from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar_url = models.URLField(
        verbose_name="Avatar URL", null=True, blank=True)

    def __str__(self):
        return self.email
