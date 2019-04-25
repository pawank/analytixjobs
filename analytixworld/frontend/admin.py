# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth import get_user_model
from frontend.models import Subscribe
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)


class SubscribeAdmin(admin.ModelAdmin):
    model = Subscribe
    list_display = ['name', 'email', 'created']
    #fields = ['name', 'email', 'created']


admin.site.register(Subscribe, SubscribeAdmin)
