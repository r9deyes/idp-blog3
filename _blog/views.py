# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def index(request):
	return render(request, '_blog/index.html')


def detail(request, article_id=None, slug=None):
	return render(request, '_blog/detail.html')


def userProfile(request, user_id=None):
	return render(request, '_blog/userProfile.html')

