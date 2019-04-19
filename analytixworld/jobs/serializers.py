from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from users.models import CustomUser
from companies.models import Company
from jobs.models import Job
# Serializers define the API representation.


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        ordering = ['-created']
