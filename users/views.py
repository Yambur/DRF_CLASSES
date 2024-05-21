from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from users.serializers import UserSerializer, PaymentSerializer, CreateUserSerializer, UserSerializerPerm
from users.models import User, Payment
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from materials.permissions import IsAuth
from users.services import create_product, create_price, create_session


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


class UserListAPIView(generics.ListAPIView):
    """Список пользователей"""
    serializer_class = UserSerializerPerm
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Подробная информация о пользователе"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Изменение пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAuth]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Удаление пользователя"""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAuth]


class PaymentListAPIView(generics.ListAPIView):
    """Список платежей"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('course_paid', 'subject_paid', 'payment_method')
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated]


class PaymentCreateAPIView(generics.CreateAPIView):
    """Создание платежа"""
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.user = self.request.user
        payment.product = create_product(product=payment.course_paid)
        payment.price = create_price(price=payment.payment_amount, product=payment.product)
        payment.session_id, payment.link, payment.status = create_session(session=payment.price)
        payment.save()
