from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import registrationForm, ProfileForm, KitchenForm, DishForm, OrderForm
from .models import User, Kitchen, Profile, Dish, Order
# Create your views here.
def landing(request):
    if request.user.is_authenticated == True:
        return render(request, 'homecooked/userIndex.html')
    else:
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
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('kitchens')
    else:
        form = ProfileForm()
    return render(request, 'homecooked/profileform.html', {'form': form})

def user_profile(request, pk):
    user = request.user
    found_profile = Profile.objects.filter(user = user).first()
    print("found Profile", found_profile)
    return render(request, 'homecooked/userProfile.html', {'profile': found_profile})

def kitchens(request):
    print('CALLING KITCHEN')
    kitchens = Kitchen.objects.all()
    dishes = Dish.objects.all()
    orders = Order.objects.filter(order_by = request.user)
    print('look here',dishes)
    return render(request, 'homecooked/userIndex.html', {'kitchens': kitchens, 'dishes': dishes, 'orders': orders})

def kitchen_detail(request, pk):
    kitchen = Kitchen.objects.get(pk=pk)
    dishes = Dish.objects.filter(kitchen = kitchen)
    orders = Order.objects.filter(order_by = request.user)
    return render(request, 'homecooked/kitchen.html', {'kitchen': kitchen, 'dishes':dishes,'orders': orders})


def kitchen_create(request):
    if request.method == 'POST':
        # form = KitchenForm(request.POST)
        form = KitchenForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('kitchens')
    else:
        form = KitchenForm()
    return render(request, 'homecooked/kitchenform.html', {'form': form})

def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            owner = request.user
            foundkitchen = Kitchen.objects.filter(owner = owner)
            post.kitchen = foundkitchen.first()
            post.save()
            return redirect('kitchens')
    else:
        form = DishForm()
    return render(request, 'homecooked/dishform.html', {'form': form})

def dish_detail(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'homecooked/dish_detail.html', {'dish':dish})

def dish_edit(request, pk):
    dish = Dish.objects.get(pk=pk)
    if request.method == "POST":
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            post = form.save(commit=False)
            owner = request.user
            foundkitchen = Kitchen.objects.filter(owner = owner)
            post.kitchen = foundkitchen.first()
            post.save()
            return redirect('kitchen', pk=dish.kitchen.pk)
    else:
        form = DishForm(instance=dish)
    return render(request, 'homecooked/dishform.html', {'form': form})

def dish_delete(request, pk):
    print('LOOK AT ME HERE!',request)
    redirectkitchen = Dish.objects.filter(kitchen_id = pk).first()
    Dish.objects.get(pk=pk).delete()
    return redirect('kitchen', pk=redirectkitchen)

def add_dish_to_cart(request, pk):
    redirectkitchen =  Dish.objects.get(pk=pk).kitchen
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            print("Home KITCHEN LOOK: =>", Dish.objects.get(pk=pk).kitchen)
            post = form.save(commit=False)
            post.order_by = request.user
            post.order_from = Dish.objects.get(pk=pk).kitchen
            post.order_item = Dish.objects.get(pk=pk)
            post.save()
            return redirect('kitchen', pk=redirectkitchen.pk)
    return redirect('kitchen', pk=redirectkitchen.pk)