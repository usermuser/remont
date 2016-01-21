# coding: utf-8
from django.conf.urls import patterns, url

#from .apple_app import views
from . import views

urlpatterns = [
    # ex: /devices/
    url(r'^$', views.index, name='index'),
    # ex: /devices/5/
    url(r'^prices(?P<device_id>\d+)/$', views.detail, name='detail'),
    # ex: /devices/5/results/
]