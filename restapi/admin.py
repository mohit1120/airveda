# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import device, temperature, humidity

admin.site.register(device)
admin.site.register(temperature)
admin.site.register(humidity)
# Register your models here.
