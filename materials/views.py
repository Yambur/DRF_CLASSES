from rest_framework import viewsets, generics

from materials.serializers import CourseSerializer, SubjectSerializer
from materials.models import Course, Subject


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class SubjectCreateAPIView(generics.CreateAPIView):
    serializer_class = SubjectSerializer


class SubjectListAPIView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SubjectRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SubjectUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SubjectDestroyAPIView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
