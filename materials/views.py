from rest_framework import viewsets, generics

from materials.serializers import CourseSerializer, SubjectSerializer
from materials.models import Course, Subject
from rest_framework.permissions import IsAuthenticated
from materials.permissions import IsModerator, IsNotModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModerator, IsNotModerator]


class SubjectCreateAPIView(generics.CreateAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, IsModerator]


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
