# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length = 255)
	short_content = models.TextField(max_length = 3000)
	content = models.TextField()
	creation_date = models.DateTimeField('date published')

