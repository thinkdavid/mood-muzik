from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from login.models import User
# Create your views here.
def index(request):
	return HttpResponse("Hello, world.")

def success(request):
	return HttpResponse("You've successfully logged in. How are you?")

def authenticate(request, user_id=None):
	last_user = User.objects.order_by('-last_login')[:1]
	last_user = last_user[0]
	context = {
		'last_user':last_user
	}
	return render(request, 'login/index.html', context)
