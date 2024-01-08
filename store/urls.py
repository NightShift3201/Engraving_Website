from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('menu/', views.menu, name ="menu"),
    path('package/', views.packages, name ="packages"),
    path('products/', views.individual_products, name ="individual_products"),
    path('cart/', views.cart, name ="cart"),
    path('checkout/', views.checkout, name ="checkout"),
]