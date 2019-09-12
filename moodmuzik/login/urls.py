# urls.py

from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('success', views.success, name='success'),
	path('authenticate/<int:user_id>', views.authenticate, name='authenticate'),
	path('authenticate', views.authenticate, name='authenticate'),
]