from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *
from .utils import cookieCart


# Create your views here.

def home(request):
    return render(request, 'store/home.html')

def menu(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems=order['get_cart_items']


    packages = Package.objects.all()
    context = {'packages': packages, 'cartItems':cartItems}
    return render(request, 'store/menu.html', context)

def packages(request, package_name):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']

    package = Package.objects.get(name=package_name)
    context = {'package': package, 'cartItems':cartItems}
    return render(request, 'store/packages.html', context)

def individual_products(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'store/individual_products.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        cartItems = cookieData['items']


    context = {'items': items, 'order':order, 'cartItems':cartItems}

    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        cartItems = cookieData['items']

    context = {'items': items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action =='add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity-1)
    
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)