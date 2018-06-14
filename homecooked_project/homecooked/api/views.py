from django.contrib.auth.models import User, Group #getting models instance 
from homecooked.models import Profile, Kitchen,Dish, Order
from rest_framework import viewsets #getting viewsets
from .serializers import UserSerializer, GroupSerializer, ProfileSerializer,KitchenSerializer,DishSerializer,OrderSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class KitchenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer

class DishViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer