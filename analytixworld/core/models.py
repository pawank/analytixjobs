from django.contrib.auth.models import AbstractUser, User
from django.db import models
from users.models import CustomUser
from django.utils import timezone


class Core(models.Model):
    change_title = models.CharField(verbose_name="Changes done",
                                    max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=False, null=True, blank=True)
    created_by = models.ForeignKey(
        'users.customuser', related_name='all_owners', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        'users.customuser', related_name='created_by', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('-updated_on', '-created_on',)
        #verbose_name_plural = "Job"
        #abstract = True

    def __str__(self):
        return self.change_title

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        super().save(*args, **kwargs)
