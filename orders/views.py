from django.shortcuts import render
from django.http import HttpResponse

from orders.models import Order


def list_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'orders/list-orders.html', context=context)

def create_order(request):
    Order.objects.create(client='Juan', product='Coca Cola', payment_method='card')
    return HttpResponse('Order created')
   
