from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='номер телефона', null=True, blank=True)
    city = models.CharField(max_length=80, verbose_name='город', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []