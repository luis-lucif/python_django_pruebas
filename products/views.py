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
   print(all_products)
   context = {
    'products': all_products,
  }
   return render(request, 'list_products.html', context=context)
 
def list_categories(request):
  all_categoryes = category.objects.all() 
  context = {
    'categories': all_categoryes,
  }
  return render(request, 'list_categories.html', context=context)

def create_category(request, name):
    category.objects.create(name=name)
    return HttpResponse('se creo la nueva categoria')
 
 
