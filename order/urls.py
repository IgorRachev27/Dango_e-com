from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.CheckOut, name='checkout'),
    path('order/', views.YourOrder, name='order'),
]