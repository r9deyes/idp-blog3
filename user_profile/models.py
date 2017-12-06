# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(to=User, on_delete=models.CASCADE, unique=True)
	avatar = models.FileField(upload_to='uploads/',null=True)
	phone = models.CharField(max_length=25,null=True)
	skype = models.CharField(max_length=100, null=True)