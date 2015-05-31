from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^devices/$', views.devices, name='devices'),
    url(r'^devices/(?P<identifier>[0-9]+)$', views.device_by_id, name='devicebyid')
]
