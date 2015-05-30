from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^/$', views.devices, name='devices'),
	url(r'^/(?P<id>[0-9]+)$', views.devicebyid, name='devicebyid')
]
