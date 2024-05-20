from rest_framework import serializers
from materials.models import Course, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    subject_count = serializers.SerializerMethodField()
    subject = SubjectSerializer(source='subject_set', many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    def get_subject_count(self, obj):
        return obj.subject_set.count()

    class Meta:
        model = Course
        fields = '__all__'
