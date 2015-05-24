from django.shortcuts import render
from django.http import HttpResponse

def devices(request):
	return HttpResponse("Hello world. This will be a list of devices")
