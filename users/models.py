from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(max_length=10, verbose_name='номер телефона', blank=True, null=True,
                                    help_text='Введите номер телефона')
    city = models.CharField(max_length=30, verbose_name='имя пользователя', blank=True, null=True,
                            help_text='Введите имя пользователя')

    USERNAME_FIELD = 'email'  # Новое поле для аутентификации
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
