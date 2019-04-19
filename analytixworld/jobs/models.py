from django.contrib.auth.models import AbstractUser, User
from django.db import models
from users.models import CustomUser


class Job(models.Model):
    title = models.CharField(verbose_name="Job Title",
                             max_length=255, null=True, blank=False)
    info_url = models.URLField(
        verbose_name="Job Information URL", null=True, blank=True)
    owner = models.ForeignKey(
        'users.customuser', related_name='jobs', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
