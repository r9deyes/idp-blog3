# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic

from user_profile.models import UserProfile
from _blog.models import Article


def userProfile(request, field=None, command=None):
	user = get_user(request)
	userProf = UserProfile.objects.get(user=user)
	if command == 'edit':
		if field in ( 'avatar', 'skype', 'phone'):
			userProf.__dict__[field] = request.POST[field]
			userProf.save()
		elif field in ('first_name', 'last_name'):
			user.__dict__[field] = request.POST[field]
			user.save()
		elif field == 'password':
			user.set_password(request.POST[field])
	if field is None or command is None:
		userObject = {'user':user, 'userProfile': userProf}
	else:
		userObject=None
	return render(request,'userProfile/index.html', userObject)


def PubList(request,**kwargs):
	return render(request,'userProfile/pubList.html')