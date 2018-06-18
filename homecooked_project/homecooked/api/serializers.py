from django.contrib.auth.models import User, Group
from homecooked.models import Profile, Kitchen, Dish, Order
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Profile
        fields = ('url','pk','user', 'name','avatar','bio', 'iscook', 'address')
        read_only_fields = ['pk', 'user']
        
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

class KitchenSerializer(serializers.ModelSerializer):
   url         = serializers.SerializerMethodField(read_only=True)
   class Meta:
        owner = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='user-detail')
        model = Kitchen
        fields = ('url', 'pk','owner', 'name','logo', 'description','address', 'rating', 'does_deliver')
        read_only_fields = ['pk', 'owner']
   def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

class DishSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Dish
        fields = ('pk','kitchen', 'name','image', 'description', 'price', 'cuisine_type', 'dietary')
        read_only_fields = ['pk', 'kitchen']
    
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

class OrderSerializer(serializers.ModelSerializer):
    order_by = serializers.ReadOnlyField(source='owner') 
    Kitchen  = serializers.ReadOnlyField(source='order_from') 

    class Meta:
        model = Order
        fields = ('pk','order_by', 'order_from','order_time', 'items')
        read_only_fields = ['pk']
    
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)