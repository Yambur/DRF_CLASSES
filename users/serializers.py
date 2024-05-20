from rest_framework import serializers
from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'city', 'payment', 'email']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializerPerm(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'city', 'email']
