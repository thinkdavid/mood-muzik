# urls.py

from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
	path('', views.index, name='index'),
	path('success', views.success, name='success'),
	path('authenticate/', views.authenticate, name='authenticate'),
]