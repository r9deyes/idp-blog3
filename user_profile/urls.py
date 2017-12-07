from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^(?P<command>\w*)/?$', views.userProfile, name='userProfile'),
	url(r'^edit/', views.editUserProfile, name='editUserProfile'),
	url(r'^publications/(order/)?(?P<field>\w*)', views.PubList, name='publications'),
]
