from users.apps import UsersConfig
from django.urls import path
from users.views import UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserListAPIView, UserDestroyAPIView, \
    PaymentListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    path('create', UserCreateAPIView.as_view(), name='user_create'),
    path('', UserListAPIView.as_view(), name='users_list'),
    path('detail/<int:pk>', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('edit/<int:pk>', UserUpdateAPIView.as_view(), name='user_edit'),
    path('delete/<int:pk>', UserDestroyAPIView.as_view(), name='user_delete'),

    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    #path('payment/create', PaymentCreateAPIView.as_view(), name='payment_create'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
