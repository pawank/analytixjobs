from rest_framework import routers, serializers, viewsets
from users.views import UserViewSet, GroupViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/groups', GroupViewSet)
