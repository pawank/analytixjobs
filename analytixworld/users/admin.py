from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name',
                    'username', 'email', 'avatar_url']


admin.site.register(CustomUser, CustomUserAdmin)
