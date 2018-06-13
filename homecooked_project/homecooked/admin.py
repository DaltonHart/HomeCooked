from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Kitchen, Dish, Order

admin.site.register(Profile)
admin.site.register(Kitchen)
admin.site.register(Dish)
admin.site.register(Order)
