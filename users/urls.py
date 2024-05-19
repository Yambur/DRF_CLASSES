from users.apps import UsersConfig
from django.urls import path
from users.views import UserCreateAPIView,UserRetrieveAPIView,UserUpdateAPIView,UserListAPIView,UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('create', UserCreateAPIView.as_view(), name='user_create'),
    path('', UserListAPIView.as_view(), name='users_list'),
    path('detail/<int:pk>', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('edit/<int:pk>', UserUpdateAPIView.as_view(), name='user_edit'),
    path('delete/<int:pk>', UserDestroyAPIView.as_view(), name='user_delete'),
]