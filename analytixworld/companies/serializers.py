from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from users.models import CustomUser
from companies.models import Company
# Serializers define the API representation.


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        ordering = ['-created_on']
