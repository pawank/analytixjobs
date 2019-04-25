from django.shortcuts import render

from rest_framework import routers, serializers, viewsets
from users.models import CustomUser
from django.contrib.auth.models import Group
from jobs.models import Job
from jobs.serializers import JobSerializer
from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-created_on')
    serializer_class = CompanySerializer
