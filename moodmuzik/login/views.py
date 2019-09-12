from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, QueryDict
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from login.models import User

import requests, json

# Create your views here.
def index(request):
	context = {}
	return render(request, 'login/authenticate_form.html', context)

def success(request):
	QDict = QueryDict(request.META['QUERY_STRING'])
	# http://localhost:8000/login/success?code=AQDsXAPUQLOi_X4A38AtCf4Jr_mrmy-T6ROgT8JB_Z3lFcv6CNLG1GeEwunxM25OVQwvSZ6v2ROp7aiyyb9cISmAtjg9kdvxn1L4AAQnZrgxRJkx_T5pRHcKvDn_syp99pDzyPHQv9aG_pQDkDEh53XiRD64A6JuBHQKSqG358n-W2S946nZOutIZmQs6ZMCsJ5MlubGwbBinpY&state=v4hKjRHJWYkGUhin
	state = QDict.get('state')
	code = QDict.get('code', default=False)
	error = QDict.get('error', default=False)

	client_id = '77bf03d75ce441e38287e089b1cb4e4c'
	client_secret = '8050567645e74a9aa3d2774647848b63'
	to_encode = client_id + ':' + client_secret

	url = 'https://accounts.spotify.com/api/token'
	body = {'grant_type': 'authorization_code', 'redirect_uri': 'localhost:8000/login/success', 'code': code}
	headers = {'Authorization': 'Basic ' + to_encode}
	print(headers)
	print(body)
	resp = requests.post(url, data=body, headers=headers)
	
	print("RESULTS OF POST REQUEST")
	# print(resp.text)
	print(resp.status_code)
	# print(resp.headers)

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

	# TO DO make this easier
	authorize_call = {\
	'client_id': client_id,\
	'redirect_uri': redirect_uri,\
	'response_type': response_type, \
	'show_dialog': show_dialog,\
	'scope': ' '.join(scope)\
	 }
	
	url = "https://accounts.spotify.com/authorize?response_type=code&client_id=77bf03d75ce441e38287e089b1cb4e4c&scope=&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Flogin%2Fsuccess&state=v4hKjRHJWYkGUhin&show_dialog=true"
	return HttpResponseRedirect(url)