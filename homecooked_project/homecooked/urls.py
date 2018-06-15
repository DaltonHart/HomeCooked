
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile_create, name='profile'),
    path('kitchens/', views.kitchen, name='kitchen'),
    path('kitchenform/', views.kitchen_create, name='kitchenForm'),
    path('dishform/', views.dish_create, name='dishForm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)