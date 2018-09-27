from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'login'

urlpatterns = [

    path('',  views.login, name='login'),
    path('auth/', include('social_django.urls'), name='social')
]