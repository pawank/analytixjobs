from django.shortcuts import render

from rest_framework import routers, serializers, viewsets
from users.models import CustomUser
from users.serializers import UserSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
