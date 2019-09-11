from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse("Hello, world.")

def success(request):
	return HttpResponse("You've successfully logged in. How are you?")