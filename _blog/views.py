# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user
from django.shortcuts import render


# Create your views here.
from _blog.apps import BlogConfig
from _blog.models import Article
from user_profile.models import UserProfile


def index(request):
	return render(request, '_blog/index.html',{'articles': Article.objects.order_by('-creation_date'),
											   'user': get_user(request),
											   'config': {'title':'TeamBlog'}})


def detail(request, article_id=None, slug=None):
	article=None
	if article_id is not None:
		article = Article.objects.get(pk=article_id)
	elif slug is not None:
		article = Article.objects.get(slug=slug)
	return render(request, '_blog/detail.html',{'article':article})


#def userProfile(request, user_id=None):
#	return render(request, '_blog/userProfile.html')

