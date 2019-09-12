from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from login.models import User

import requests
# Create your views here.
def index(request):
	context = {}
	return render(request, 'login/authenticate_form.html', context)

def success(request):
	last_user = User.objects.order_by('-last_login')[:1]
	last_user = last_user[0]

	user = get_object_or_404(User, name="David Becher")
	context = {
		'last_user':user
	}
	return render(request, 'login/index.html', context)

def authenticate(request, user_id=None):
	client_id = '77bf03d75ce441e38287e089b1cb4e4c'
	redirect_uri = 'localhost:8000/login/success'
	response_type = 'code'
	show_dialog = 'true'
	scope = ['user-read-private', 'user-read-email', 'streaming', 'user-read-currently-playing']

	authorize_call = {\
	'client_id': client_id,\
	'redirect_uri': redirect_uri,\
	'response_type': response_type, \
	'show_dialog': show_dialog,\
	'scope': ' '.join(scope)\
	 }
	
	resp = requests.get("https://accounts.spotify.com/authorize", params=authorize_call)
	return HttpResponseRedirect(resp.url)