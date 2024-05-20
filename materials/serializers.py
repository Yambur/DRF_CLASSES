from rest_framework import serializers
from materials.models import Course, Subject, Subscription
from materials.validators import LinkValidator


class SubjectSerializer(serializers.ModelSerializer):
    validators = [LinkValidator(field='link')]

    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    subject_count = serializers.SerializerMethodField()
    subject = SubjectSerializer(source='subject_set', many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    def get_subject_count(self, obj):
        return obj.subject_set.count()

    def get_subscription(self, obj):
        request = self.context.get('request')
        user = None
        if request:
            user = request.user
        return obj.subscription_set.filter(user=user).exists()

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
