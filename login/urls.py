from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'login'

urlpatterns = [

    path('',  views.login, name='login'),
    path('auth/', include('social_django.urls'), name='social'),
    path('profile/',  views.home, name='home'),
    path('volunteer', views.login_volunteer, name="volunteer_login"),
    path('victim/', views.login_victim, name="victim_login"),
    path('ngo', views.login_ngo, name="ngo_login")

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)