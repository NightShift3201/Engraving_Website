from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'store/home.html')

def menu(request):
    return render(request, 'store/menu.html')

def packages(request):
    return render(request, 'store/packages.html')

def individual_products(request):
    return render(request, 'store/individual_products.html')

def checkout(request):
    return render(request, 'store/checkout.html')