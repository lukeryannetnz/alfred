''' contains view controllers for the alfred api '''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import OnOffSwitch

def index(request):
    ''' renders the default app index. TODO move this '''
    return render(request, 'index.html', None)

def devices(request):
    ''' Returns the full list of device objects. '''
    switches = OnOffSwitch.objects.all()
    return JsonResponse(serializers.serialize('json', switches), safe=False)

@csrf_exempt
def device_by_id(request, identifier):
    ''' Returns a single device by its primary key identifier '''
    if request.method == 'GET':
        switch = get_object_or_404(OnOffSwitch, pk=identifier)

        return JsonResponse(serializers.serialize('json', [switch, ]), safe=False)

    elif request.method == 'PATCH':
        switch = OnOffSwitch.objects.get(pk=identifier)
        if request.body == 'toggle':
            switch.toggle_state()
            return HttpResponse()
    else:
        return HttpResponseBadRequest()
