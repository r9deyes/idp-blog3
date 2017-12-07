# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user
from django.shortcuts import render, get_object_or_404

# Create your views here.
from _blog.apps import BlogConfig
from _blog.models import Article
from user_profile.models import UserProfile

static_server = 'https://r9deyes.github.io/idp-blog3/static/'

def index(request):
	return render(request, '_blog/index.html',{'articles': Article.objects.order_by('-creation_date'),
											   'user': get_user(request),
											   'config': {'title':'TeamBlog'},
											   'static_url': static_server})


def detail(request, article_id=None, slug=None):
	article=None
	if article_id is not None:
		article = get_object_or_404(Article, pk=article_id)
	elif slug is not None:
		article = get_object_or_404(Article, slug=slug)
	return render(request, '_blog/detail.html',{'article':article, 'static_url': static_server})


#def userProfile(request, user_id=None):
#	return render(request, '_blog/userProfile.html')

