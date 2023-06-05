from django.shortcuts import render
from django.views import View
from .models import MenuItem, Category, OrderModel

# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Customer/index.html')


class Ooder(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')

        # pass into context
        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks
        }

        #render the template
        return render(request, 'Customer/order.html', context)
    