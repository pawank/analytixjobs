from django.contrib.auth.models import AbstractUser, User
from django.db import models
from core.models import Core
from users.models import CustomUser
from companies.models import Company


class Job(Core):
    title = models.CharField(verbose_name="Job Title",
                             max_length=255, null=True, blank=False)
    info_url = models.URLField(
        verbose_name="Job Information URL", null=True, blank=True)
    employer = models.ForeignKey(
        'companies.company', related_name='employers', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_on', 'title',)
        #verbose_name_plural = "Job"
        pass

    def __str__(self):
        return self.title
