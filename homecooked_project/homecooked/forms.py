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
    iscook = forms.BooleanField(required=False)
    class Meta:
        model = Profile
        fields = ('name', 'avatar','bio','address', 'iscook')

#Form(request.POST, request.FILES, instance = company)
class KitchenForm(forms.ModelForm):

    class Meta:
        model = Kitchen
        exclude = ["user"]
        fields = ('name', 'logo','description','address')

class DishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ('name', 'image','description','price','cuisine_type')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_by', 'order_from','order_item','items')