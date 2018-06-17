from django.contrib.auth.models import User, Group
from homecooked.models import Profile, Kitchen, Dish, Order
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'name','avatar','bio', 'iscook', 'address')
        
class KitchenSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
        model = Kitchen
        fields = ('owner', 'name','logo', 'description','address', 'rating', 'does_deliver')

class DishSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Dish
        fields = ('kitchen', 'name','image', 'description', 'price', 'cuisine_type', 'dietary')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_by = serializers.ReadOnlyField(source='owner') 
    Kitchen  = serializers.ReadOnlyField(source='order_from') 

    class Meta:
        model = Order
        fields = ('order_by', 'order_from','order_time', 'items')

