from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^.*devices$', views.devices, name='devices'),
	url(r'.*devices/.*^$', views.devicebyid, name='devicebyid')
]

