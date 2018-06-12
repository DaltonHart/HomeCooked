from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Kitchen

admin.site.register(Profile)
admin.site.register(Kitchen)

