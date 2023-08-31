from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(resquest) :
    return render(resquest, 'index.html', context={})

def hola_mundo(resquest) :
    return HttpResponse("hola mundo")

def otra_mas(resquest) :
    return HttpResponse('otra masss')

def fecha_actual (resquest) :
    hoy = datetime.now().date()
    return HttpResponse (f'la fecha de hoy es {hoy}')

def vista_con_edad(resquest, edad):
    return HttpResponse(f'esto funciona? la edad es la {edad}')


def vista_con_template(request):
    return render(request, 'template.html', context={})

def saludo_desde_template(request):
    
    context= {
        'nombre': 'luis',
        'edad' : 37,
        'lista_frutas' :  ['manzana','pera', 'banana', 'naranja'],
        
    } 
    return render(request, 'saludo.html', context=context)