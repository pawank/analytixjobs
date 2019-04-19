from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import CustomUser


class Company(models.Model):
    name = models.CharField(verbose_name="Company name", max_length=255,
                            null=True, blank=False)
    registered_name = models.CharField(verbose_name="Registered Company name", max_length=255,
                                       null=True, blank=True)
    no_employees = models.IntegerField(verbose_name="No of Employees",
                                       null=True, blank=True)
    website = models.URLField(
        verbose_name="Website", null=True, blank=True)
    owner = models.ForeignKey(
        'users.customuser', related_name='companies', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
