from django.shortcuts import render

from rest_framework import routers, serializers, viewsets
from users.models import CustomUser
from django.contrib.auth.models import Group
from jobs.models import Job
from jobs.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-created')
    serializer_class = JobSerializer
