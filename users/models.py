from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Subject


class User(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='номер телефона', null=True, blank=True)
    city = models.CharField(max_length=80, verbose_name='город', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    cash = "Наличные"
    transfer = "Перевод на счёт"
    payment_methods = [
        (cash, "Наличные"), (transfer, "Перевод на счёт")]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateField(verbose_name='дата оплаты')
    course_paid = models.ForeignKey(Course, verbose_name='оплаченный курс', on_delete=models.CASCADE)
    subject_paid = models.ForeignKey(Subject, verbose_name='оплаченный урок', on_delete=models.CASCADE)
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50, default=transfer, choices=payment_methods)

    def __str__(self):
        return f'У {self.user} дата оплаты {self.payment_date}'

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
