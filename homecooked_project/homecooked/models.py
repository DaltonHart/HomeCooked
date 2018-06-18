from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.templatetags.static import static
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userprofile')
	name = models.CharField(blank=True, max_length=255)
	avatar = models.ImageField(upload_to = 'img/', default = 'img/None/no-img.gif')
	bio = models.TextField()
	iscook = models.BooleanField(default=False)
	address = models.TextField()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
	    
	def get_api_url(self, request=None):
		return api_reverse("homecooked-api:profile-rud", kwargs={'pk': self.pk}, request=request)

class Kitchen(models.Model):
	owner = models.OneToOneField(User,
        on_delete=models.CASCADE,
        primary_key=True,parent_link=True)
	# owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='owner')
	name = models.CharField(blank=True, max_length=60)
	logo = models.ImageField(upload_to = 'img/', default = 'img/None/no-img.gif')
	description = models.TextField(max_length=140)
	address = models.TextField()
	rating = models.IntegerField( null=True, blank=True)
	does_deliver = models.BooleanField(default=False)


	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

	def get_api_url(self, request=None):
		return api_reverse("homecooked-api:kitchen-rud", kwargs={'pk': self.pk}, request=request)


class Dish(models.Model):
	kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='dish')
	name = models.CharField(blank=True, max_length=60)
	image = models.ImageField(upload_to = 'img/', default = 'img/None/no-img.gif')
	description = models.TextField(max_length=140)
	price = models.FloatField()
	cuisine_type = models.CharField(max_length=15) 
	dietary = ArrayField(models.CharField(max_length=10), null=True)


	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

	def get_api_url(self, request=None):
		return api_reverse("homecooked-api:dish-rud", kwargs={'pk': self.pk}, request=request)




class Order(models.Model):
	order_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_by')
	order_from = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='order_from')
	order_time = models.DateTimeField(auto_now_add=True)
	items = ArrayField(models.CharField(blank=True, max_length=60))

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-order_by']
	def get_api_url(self, request=None):
		return api_reverse("homecooked-api:order-rud", kwargs={'pk': self.pk}, request=request)
