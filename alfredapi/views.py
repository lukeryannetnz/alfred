''' contains view controllers for the alfred api '''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import OnOffSwitch

def devices(request):
    ''' Returns the full list of device objects. '''
    switches = OnOffSwitch.objects.all()
    values = []

    for switch in switches:
        s = {}
        s['pk'] = switch.pk
        s['location'] = switch.location
        s['description'] = switch.description
        s['image'] = switch.image_url
        values.append(s)

    return JsonResponse({'items' : values }, safe=False)

@csrf_exempt
def device_by_id(request, identifier):
    ''' Returns a single device by its primary key identifier '''
    if request.method == 'GET':
        switch = get_object_or_404(OnOffSwitch, pk=identifier)

        return JsonResponse(dict(pk=switch.pk, location=switch.location, description=switch.description, image=switch.image_url), safe=False)

    elif request.method == 'PATCH':
        switch = OnOffSwitch.objects.get(pk=identifier)
        if request.body == 'toggle':
            switch.toggle_state()
            return HttpResponse()
    else:
        return HttpResponseBadRequest()
