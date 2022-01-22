from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpRequest
#from .forms import createAccountForm
from django.urls import path
from django.conf import settings
from django.utils import timezone
import datetime

from skimhome.models import SiteModel
from urllib.parse import urlencode
#from zenusers.views import profile_data as profile_data
import json, requests
import os
from pathlib import Path
# Create your views here.

def home(request):		
	print("display home page")
	return render(request,'home.html',{})

def login(request):
	print("display login page")
	return render(request,'login.html',{})

def aboutus(request):
	print("display learn more/ aboutus")
	return render(request,'aboutus.html',{})





#	clientid = models.AutoField(primary_key=true)
#    name = models.CharField(max_length=100)
#    role = models.CharField(max_length=50)
#    createddate = models.DateTimeField()
#    logintype = models.IntegerField()
#subdomain is the name of the company zendesk url
#    subdomain = models.CharField(max_length=100)