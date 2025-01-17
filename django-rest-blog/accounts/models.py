from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("Email address", unique=True)
    age = models.PositiveSmallIntegerField(null=False, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["age"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
