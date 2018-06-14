from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.templatetags.static import static
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
	name = models.CharField(blank=True, max_length=255)
	avatar = models.ImageField(upload_to = 'img/', default = 'img/None/no-img.gif')
	bio = models.TextField()
	iscook = models.BooleanField(default=False)
	address = models.TextField()

	def __str__(self):
		return self.username

	class Meta:
		ordering = ['name']

class Kitchen(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kitchen')
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

class Dish(models.Model):
	kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='dish')
	name = models.CharField(blank=True, max_length=60)
	image = models.ImageField(upload_to = 'img/', default = 'img/None/no-img.gif')
	description = models.TextField(max_length=140)
	price = models.FloatField()
	cuisine_type = models.CharField(max_length=15) 
	dietary = ArrayField(models.CharField(max_length=10))


	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']



class Order(models.Model):
	order_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_by')
	order_from = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='order_from')
	order_time = models.DateTimeField(auto_now_add=True)
	items = ArrayField(models.CharField(blank=True, max_length=60))

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-order_by']
