from rest_framework import routers, serializers, viewsets
from users.views import UserViewSet, GroupViewSet
from companies.views import CompanyViewSet
from jobs.views import JobViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'v1/users', UserViewSet)
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/companies', CompanyViewSet)
router.register(r'v1/jobs', JobViewSet)
