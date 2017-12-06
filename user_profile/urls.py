from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^(?P<field>\w*)/?(?P<command>\w*)/?$', views.userProfile, name='userProfile'),
	url(r'^publications/', views.PubList, name='publications'),
]
