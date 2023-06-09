from django.urls import path
from .views import Index, Order, OrderConfirmation

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('order/', Order.as_view(), name="order"), 
    path('order-confirmation/', OrderConfirmation.as_view(), name="order_confirmation") 
]
