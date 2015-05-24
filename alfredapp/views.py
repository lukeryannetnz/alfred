from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from .models import OnOffSwitch

def devices(request):
	switches =  OnOffSwitch.objects.all()
	return JsonResponse(serializers.serialize('json', switches), safe=False)
