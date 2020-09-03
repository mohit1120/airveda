"""airveda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^display/', views.display),
    url(r'^api/deviceadd/', views.deviceAdd.as_view()),
    url(r'^api/deviceone/(?P<id>\d+)/$', views.deviceOne.as_view()),
    url(r'^api/devicelist', views.deviceList.as_view()),
    url(r'^api/deviceremove/(?P<id>\d+)/$', views.deviceRemove.as_view()),
    

    #for Temperature
    url(r'^api/temperaturelist/(?P<id>\d+)/$', views.temperatureList.as_view()),
    url(r'^api/temperatureadd', views.temperatureAdd.as_view()),

    #for Humidity
    url(r'^api/humiditylist/(?P<id>\d+)/$', views.humidityList.as_view()),
    url(r'^api/humidityadd', views.humidityAdd.as_view()),


]
