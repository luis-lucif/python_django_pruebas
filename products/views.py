from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products, category



# Create your views here.

def create_product(request):
    new_product = Products.objects.create(name='monster ', price=600, stock=True)
    print(new_product)
    return HttpResponse('se creo el nuevo producto')

def list_products(request):
   all_products = Products.objects.all()
   context = {
    'products': all_products,
  }
   return render(request, 'products/list_products.html', context=context)
 
def list_categories(request):
  all_categories = category.objects.all() 
  context = {
    'categories': all_categories,
  }
  return render(request, 'categories/list_categories.html', context=context)

def create_category(request, name):
    category.objects.create(name=name)
    return HttpResponse('se creo la nueva categoria')
 
 
