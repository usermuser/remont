# coding: utf-8
from django.contrib import admin
from apple_app.models import Device, Usluga

class UslugaAdmin(admin.ModelAdmin):
    list_display = ('device', 'service_type', 'service_price', 'service_time')

admin.site.register(Device)
admin.site.register(Usluga, UslugaAdmin)

