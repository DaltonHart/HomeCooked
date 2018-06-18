
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile_create, name='profile'),
    path('kitchens/', views.kitchens, name='kitchens'),
    path('kitchens/<int:pk>', views.kitchen_detail, name='kitchen'),
    path('kitchenform/', views.kitchen_create, name='kitchenForm'),
    path('dishform/', views.dish_create, name='dishForm'),
    path('dishes/<int:pk>', views.dish_detail, name='dish'),
    path('dishes/<int:pk>/delete', views.dish_delete, name='dish_delete'),
    path('dishes/<int:pk>/edit', views.dish_edit, name='dish_edit'),
    path('userprofile/<int:pk>', views.user_profile, name='user_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)