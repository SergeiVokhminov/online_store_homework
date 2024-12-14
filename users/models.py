from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите email")
    avatar = models.ImageField(
        upload_to="photo/avatars/", blank=True, null=True, verbose_name="Аватар", help_text="Загрузите изображение"
    )
    phone_number = models.CharField(blank=True, null=True, verbose_name="Телефон", help_text="Введите номер телефона")
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name="Страна", help_text="Введите страну")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # "username",

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
