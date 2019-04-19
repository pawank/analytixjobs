from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Job
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)


class JobAdmin(admin.ModelAdmin):
    model = Job


admin.site.register(Job, JobAdmin)
