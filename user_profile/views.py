# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from django.urls import reverse
from django.views import generic

from user_profile.models import UserProfile
from _blog.models import Article


def userProfile(request, command=None):
	user = get_user(request)
	userProf = UserProfile.objects.get(user=user)
	userObject = {'user': user, 'userProfile': userProf}
	#else:
	#return render(request, '/accounts/profile.html', userObject)
	return render(request, 'userProfile/index.html', userObject)


def PubList(request, **kwargs):
	publist = []
	if kwargs['field'] == 'creationDate':
		publist = get_list_or_404(Article,author=get_user(request))
		publist.order_by('')
	return render(request, 'userProfile/pubList.html')


def editUserProfile(request):
	user = get_user(request)
	userProf = UserProfile.objects.get(user=user)
	#for field in ('skype', 'phone'):
	userProf.skype = request.POST['skype']
	userProf.phone= request.POST['phone']
	print(request.POST)
	#	userProf.setattr(field, request.POST.getattr(field))
	userProf.save()
	for field in ('first_name', 'last_name'):
		user.setattr(field, request.POST.getattr(field))
	user.save()
	if request.POST.hasattr('pass'):
		user.set_password(request.POST.getattr('pass'))
	userObject = {'user': user, 'userProfile': userProf}
	return render(request, 'userProfile/index.html',userObject)