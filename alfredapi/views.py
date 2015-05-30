from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .models import OnOffSwitch

def index(request):
	return render(request, 'index.html', None)

def devices(request):
	switches =  OnOffSwitch.objects.all()
	return JsonResponse(serializers.serialize('json', switches), safe=False)

@csrf_exempt
def devicebyid(request, id):
	if(request.method == 'GET') :
		switch = OnOffSwitch.objects.filter(pk=id)
		return JsonResponse(serializers.serialize('json', switch), safe=False)

	elif(request.method == 'PATCH') :
		switch = OnOffSwitch.objects.get(pk=id)
		if(request.body == 'toggle') :
			switch.toggle()
			return HttpResponse()
	else :
		return HttpResponseBadRequest()
