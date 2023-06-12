from django.urls import path
from .views import Index, Order, OrderConfirmation, OrderPayConfirmation

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('order/', Order.as_view(), name="order"), 
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(), name="order-confirmation"), 
    path('payment-confirmation/', OrderPayConfirmation.as_view(), name="payment-submitted"),
]
