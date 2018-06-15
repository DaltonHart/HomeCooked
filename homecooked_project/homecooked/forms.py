from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Kitchen, Dish, Order
from django.forms import CharField, Form, PasswordInput

class registrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def save(self, commit=True):
        user = super(registrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'avatar','bio','address')

class KitchenForm(forms.ModelForm):

    class Meta:
        model = Kitchen
        fields = ('name', 'logo','description','address')

class DishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ('name', 'image','description','price','cuisine_type')