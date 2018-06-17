from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, ProfileViewSet, KitchenViewSet, DishViewSet,OrderViewSet



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'kitchens', KitchenViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'orders', OrderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
 url(r'^', include(router.urls))
]

