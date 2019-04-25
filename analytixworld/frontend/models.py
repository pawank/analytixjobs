# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from users.models import CustomUser
from companies.models import Company
from django.utils import timezone


class Subscribe(models.Model):
    name = models.CharField(verbose_name="Name of person",
                            max_length=255, null=True, blank=False)
    email = models.EmailField(verbose_name="Email address",
                              max_length=255, null=True, blank=False)
    owner = models.ForeignKey(
        'users.customuser', related_name='owners', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.name) + " at " + str(self.created)
