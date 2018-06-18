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
        fields = ('url','id','user', 'name','avatar','bio', 'iscook', 'address')
        read_only_fields = ['id', 'user']
        
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

class KitchenSerializer(serializers.ModelSerializer):
   url         = serializers.SerializerMethodField(read_only=True)
   class Meta:
        owner = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='user-detail')
        model = Kitchen
        fields = ('url', 'id','owner', 'name','logo', 'description','address', 'rating', 'does_deliver')
        read_only_fields = ['id', 'owner']
   def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

class DishSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Dish
        fields = ('id','kitchen', 'name','image', 'description', 'price', 'cuisine_type', 'dietary')
        read_only_fields = ['id', 'kitchen']
    
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

class OrderSerializer(serializers.ModelSerializer):
    order_by = serializers.ReadOnlyField(source='owner') 
    Kitchen  = serializers.ReadOnlyField(source='order_from') 

    class Meta:
        model = Order
        fields = ('id','order_by', 'order_from','order_time', 'items')
        read_only_fields = ['id']
    
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)