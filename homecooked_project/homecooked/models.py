from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.templatetags.static import static
from django.conf import settings
from django.db import models


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
	name = models.CharField(blank=True, max_length=255)
	bio = models.TextField()
	iscook = models.CharField(blank=True, max_length=5)
	address = models.TextField()


	def __str__(self):
		return self.username

	class Meta:
		ordering = ['name']



