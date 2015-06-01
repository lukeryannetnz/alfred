''' contains view controllers for the alfred api '''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def index(request):
    ''' renders the application home page. '''
    return render(request, 'index.html', None)
