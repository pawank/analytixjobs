from django.contrib import admin
from django.contrib.auth import get_user_model
from jobs.models import Job
from companies.models import Company
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)


class CompanyAdmin(admin.ModelAdmin):
    model = Company


admin.site.register(Company, CompanyAdmin)
