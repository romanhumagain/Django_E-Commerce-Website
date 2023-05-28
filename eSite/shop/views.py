from django.shortcuts import render
from django.http import HttpResponse
from . models import product
from math import ceil
# Create your views here.
def index(request):
    products = product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'shop/index.html', params)

def about(request):
  return render(request , 'shop/about.html')

def contact(request):
  return HttpResponse("Contact Us Please for furthor information")

def tracker(request):
  return HttpResponse("Tracking your Products !!")

def search(request):
  return HttpResponse("Search your desired products !!")

def productView(request):
  return HttpResponse("Wecome to the Product Home Page")

def checkout(request):
  return HttpResponse("we are at checkout !!")