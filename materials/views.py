from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.response import Response

from materials.paginations import CoursePaginator, SubjectPaginator
from materials.serializers import CourseSerializer, SubjectSerializer, SubscriptionSerializer
from materials.models import Course, Subject, Subscription
from rest_framework.permissions import IsAuthenticated
from materials.permissions import IsModerator, IsNotModerator
from drf_yasg.inspectors import SwaggerAutoSchema


class Decorate_Viewset_Methods(SwaggerAutoSchema):
    def decorate_viewset_methods(names, decorator):
        if names == "__all__":
            names = [
                "list",
                "create",
                "retrieve",
                "update",
                "partial_update",
                "destroy",
            ]

        def decorate(cls):
            for name in names:
                method = getattr(cls, name)
                setattr(cls, name, decorator(method))
            return cls

        return decorate


@Decorate_Viewset_Methods.decorate_viewset_methods(names="__all__", decorator=swagger_auto_schema(tags=['names']))


class CourseViewSet(viewsets.ModelViewSet):
    """Класс по курсам"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModerator, IsNotModerator]
    pagination_class = CoursePaginator


class SubjectCreateAPIView(generics.CreateAPIView):
    """Создание урока"""
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, IsModerator]
    pagination_class = SubjectPaginator


class SubjectListAPIView(generics.ListAPIView):
    """Список уроков"""
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


class SubjectRetrieveAPIView(generics.RetrieveAPIView):
    """Получение информации об уроке"""
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsNotModerator]


class SubjectUpdateAPIView(generics.UpdateAPIView):
    """Изменение урока"""
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsNotModerator]


class SubjectDestroyAPIView(generics.DestroyAPIView):
    """Удаление урока"""
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsModerator, IsNotModerator]


class SubscriptionCreateView(generics.CreateAPIView):
    """Создание подписки"""
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        if Subscription.objects.filter(user=user, course=course_item).exists():
            Subscription.objects.get(user=user, course=course_item).delete()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'

        return Response({"message": message})
