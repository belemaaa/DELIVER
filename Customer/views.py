from django.shortcuts import render
from django.views import View
from .models import MenuItem, Category, OrderModel

# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Customer/index.html')


class Order(View):
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
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,

            }
            order_items['items'].append(item_data)

        # sum total price
        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            name=name,
            email=email,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            price=price
            )
        order.item.add(*item_ids)   

        context = {
            'items': order_items['items'],
            'price': price
        } 
        request.session['items'] = items
        request.session['price'] = price

        return render(request, 'Customer/order_confirmation.html', context)


