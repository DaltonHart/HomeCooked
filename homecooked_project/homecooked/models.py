from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.templatetags.static import static
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models



class CustomUser(AbstractUser):
	name = models.CharField(blank=True, max_length=255)
	bio = models.TextField()
	iscook = False
	member_date = models.DateTimeField(auto_now_add=True)
	address = models.TextField()


	def __str__(self):
		return self.username
	class Meta:
		ordering = ['name']

# class Kitchen(models.Model):
# 	name         = models.CharField(max_length=30)
# 	created_date   = models.DateTimeField(auto_now_add=False, blank=False)
	

# 	def __str__(self):
# 		return self.name
# 	class Meta:
# 		ordering = ['-start_date']