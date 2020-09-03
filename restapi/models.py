# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class device(models.Model):
    uid=models.IntegerField()
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name



class temperature(models.Model):
    uid=models.IntegerField()
    temp=models.CharField(max_length=10)
    Date=models.DateTimeField(auto_now_add=True)



class humidity(models.Model):
    uid=models.IntegerField()
    humidity=models.CharField(max_length=10)
    Date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.humidity