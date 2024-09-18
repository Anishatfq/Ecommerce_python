from django.urls import path
from . import views

urlpatterns = [
    # Define your app’s URL patterns here
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # Add other URL patterns for the `shop` app
]
