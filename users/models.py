from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    error_messages = {
        "unique": "A user with that username already exists."
    }
    email = models.EmailField("email address", blank=True)
    password = models.CharField(max_length=100)
    vegetarian = models.BooleanField(default=False)
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        swappable = "AUTH_USER_MODEL"
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username
