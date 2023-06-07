from django.urls import path
from .views import Index, Order
from . import views

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('order/', Order.as_view(), name="order"),  
    path('view/orders/', views.ViewOrders, name="view-orders") 
]
