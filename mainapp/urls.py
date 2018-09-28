from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'mainapp'

urlpatterns = [

    path('home/',  views.home, name='mainapp_home')
]