from django.contrib.auth.models import User, Group 
from django.db.models import Q 
from homecooked.models import Profile, Kitchen,Dish, Order
from rest_framework import generics, permissions,mixins 
from .serializers import ProfileSerializer,KitchenSerializer,DishSerializer,OrderSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from homecooked.api.permissions import IsOwnerOrReadOnly


class ProfileApiView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    lookup_field         = 'pk'
    serializer_class      = ProfileSerializer
    def get_queryset(self):
        all_profiles = Profile.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            all_profiles = all_profiles.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)
                    ).distinct()
        return all_profiles

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class ProfilePostRudView(generics.RetrieveUpdateDestroyAPIView): 
    lookup_field         = 'pk'
    serializer_class      = ProfileSerializer
    permission_classes      = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Profile.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}



class KitchenApiView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    lookup_field         = 'pk'
    serializer_class      = KitchenSerializer
    def get_queryset(self):
        all_kitchens = Kitchen.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            all_kitchens = all_kitchens.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)
                    ).distinct()
        return all_kitchens

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class KitchenPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field         = 'pk'
    serializer_class      = KitchenSerializer
    permission_classes   = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Kitchen.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

# class DishViewSet(mixins.CreateModelMixin, generics.ListAPIView):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Dish.objects.all()
#     serializer_class = DishSerializer

# class OrderViewSet(mixins.CreateModelMixin, generics.ListAPIView):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer