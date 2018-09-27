from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'accounts'

urlpatterns = [

    path('profile/',  views.accounts, name='accounts'),
    path('auth/', include('social_django.urls'), name='social')
]