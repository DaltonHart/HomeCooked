from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import registrationForm, ProfileForm, KitchenForm, DishForm
from .models import Profile, Kitchen, Dish

# Create your views here.
def landing(request):
    return render(request, 'homecooked/landing.html')

def signup(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = registrationForm()
    return render(request, 'homecooked/signup.html', {'form': form})

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('kitchen')
    else:
        form = ProfileForm()
    return render(request, 'homecooked/profileform.html', {'form': form})

def kitchen(request):
    kitchens = Kitchen.objects.all()
    dishes = Dish.objects.all()
    print('look here',dishes)
    return render(request, 'homecooked/userIndex.html', {'kitchens': kitchens, 'dishes': dishes})

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'homecooked/userProfile.html', {'profile': profile})

def kitchen(request):
    return render(request, 'homecooked/userIndex.html')
def kitchen_detail(request, pk):
    kitchen = Kitchen.objects.get(id=pk)
    return render(request, 'homecooked/kitchen.html', {'kitchen': kitchen})

def cook_menu(request):
    # cook_menu = Dish.objects.get(id=pk)
    return render(request, 'homecooked/cookMenu.html')

def kitchen_create(request):
    if request.method == 'POST':
        form = KitchenForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('kitchen')
    else:
        form = KitchenForm()
    return render(request, 'homecooked/kitchenform.html', {'form': form})

def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            owner = request.user
            foundkitchen = Kitchen.objects.filter(owner = owner)
            post.kitchen = foundkitchen.first()
            post.save()
            return redirect('kitchen')
    else:
        form = DishForm()
    return render(request, 'homecooked/dishform.html', {'form': form})
