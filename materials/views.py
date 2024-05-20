from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response

from materials.paginations import CoursePaginator, SubjectPaginator
from materials.serializers import CourseSerializer, SubjectSerializer, SubscriptionSerializer
from materials.models import Course, Subject, Subscription
from rest_framework.permissions import IsAuthenticated
from materials.permissions import IsModerator, IsNotModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModerator, IsNotModerator]
    pagination_class = CoursePaginator


class SubjectCreateAPIView(generics.CreateAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, IsModerator]
    pagination_class = SubjectPaginator


class SubjectListAPIView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


class SubjectRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsNotModerator]


class SubjectUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsNotModerator]


class SubjectDestroyAPIView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsModerator, IsNotModerator]


class SubscriptionCreateView(generics.CreateAPIView):
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
