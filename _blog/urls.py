from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^user/', views.userProfile, name='userProfile'),
	url(r'^blog(?P<article_id>[0-9]+)', views.detail, name='article'),
	url(r'^blog(?P<slug>[\w_\d-]+)', views.detail, name='article'),

]
