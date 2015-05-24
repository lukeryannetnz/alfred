from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.devices, name='devices'),
]

