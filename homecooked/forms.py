from django import forms
from djang.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
	class meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username', 'email', 'name', 'bio', 'iscook','address')


class CustomUserChangeForm(UserChangeForm):
	class meta(UserChangeForm.Meta):
		model = CustomUser
		fields = UserChangeForm.Meta.fields

