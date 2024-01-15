from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('menu/', views.menu, name ="menu"),
    path('package/<str:package_name>/', views.packages, name ="packages"),
    path('products/', views.individual_products, name ="individual_products"),
    path('cart/', views.cart, name ="cart"),
    path('checkout/', views.checkout, name ="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
]