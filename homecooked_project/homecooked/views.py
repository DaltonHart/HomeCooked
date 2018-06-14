from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'homecooked/landing.html')

def kitchen(request):
    return render(request, 'homecooked/userIndex.html')

