# coding: utf-8
from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    picture_name = models.CharField(max_length=200, blank=True, null=True)
  
    def __unicode__(self):  # Python 3: def __str__(self):
            return self.name

class Usluga(models.Model):
    device = models.ForeignKey(Device)
    service_type = models.CharField(max_length=300, blank=True, null=True)
    service_price = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True, default=1000)
    service_time = models.CharField(max_length=200, blank=True, null=True, default='1 час')

    def __unicode__(self):  # Python 3: def __str__(self):
            return self.service_type