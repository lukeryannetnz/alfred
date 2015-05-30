''' contains view controllers for the alfred api '''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .models import OnOffSwitch

def index(request):
    ''' renders the default app index. TODO move this '''
    return render(request, 'index.html', None)

def devices():
    ''' Returns the full list of device objects. '''
    switches = OnOffSwitch.objects.all()
    return JsonResponse(serializers.serialize('json', switches), safe=False)

@csrf_exempt
def devicebyid(request, identifier):
    ''' Returns a single device by its primary key identifier '''
    if(request.method == 'GET'):
        switch = OnOffSwitch.objects.filter(pk=identifier)
        return JsonResponse(serializers.serialize('json', switch), safe=False)

    elif(request.method == 'PATCH'):
        switch = OnOffSwitch.objects.get(pk=identifier)
        if(request.body == 'toggle'):
            switch.toggle_state()
            return HttpResponse()
    else:
        return HttpResponseBadRequest()
