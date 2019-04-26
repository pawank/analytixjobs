from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import Core
from users.models import CustomUser


class Company(Core):
    name = models.CharField(verbose_name="Company name", max_length=500,
                            null=True, blank=False)
    registered_name = models.CharField(verbose_name="Registered Company name", max_length=500,
                                       null=True, blank=True)
    no_employees = models.IntegerField(verbose_name="No of Employees",
                                       null=True, blank=True)
    website = models.URLField(
        verbose_name="Website", null=True, blank=True)

    class Meta:
        ordering = ('-created_on', 'name')
        #verbose_name_plural = "Company"

    def __str__(self):
        return self.name
