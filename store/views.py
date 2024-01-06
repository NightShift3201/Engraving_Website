from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'store/home.html')

def menu(request):
    return render(request, 'store/menu.html')

def packages(request):
    return render(request, 'store/packages.html')

def individual_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/individual_products.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items': items, 'order':order}

    return render(request, 'store/cart.html', context)