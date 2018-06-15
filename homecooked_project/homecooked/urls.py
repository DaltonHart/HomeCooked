
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile_create, name='profile'),
    path('kitchens/', views.kitchen, name='kitchen'),
    path('kitchenform/', views.kitchen_create, name='kitchenForm'),
    path('dishform/', views.dish_create, name='dishForm'),
    path('userprofile/<int:pk>', views.user_profile, name='user_profile'),
    path('cookmenu/', views.cook_menu, name='cook_menu'),
]
