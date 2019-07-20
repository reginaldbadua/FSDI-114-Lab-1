from django.shortcuts import render
from django.http import HttpResponse

from .models import Detail, Product
# Create your views here.

def index(request):
    #Product.objects.all() read the table
    inventory = Product.objects.all()
    # name = ''
    # for p in inventory:
    #     name += (p.product_name + ", ")
    return render(request, 'views/index.html', {'inventory': inventory})

def detail(request):
#     return HttpResponse("I'm a detail page  " + product_name)
        the_product = Product.objects.get(price=85)
        return render(request, 'views/detail.html', {'product': the_product})

def test(request):
    return HttpResponse("<h1>I'm a test</h1>")  #endpoint registered on production/urls.py

def contact(request):
    return HttpResponse("<h1>Page under construction</h1>") #Session 1, 2:01:52