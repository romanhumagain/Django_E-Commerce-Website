from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  return render(request, 'shop/index.html')

def about(request):
  return HttpResponse("About E-Commerce Website")

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