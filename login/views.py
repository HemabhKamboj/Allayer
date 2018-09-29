from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def login(request):
    
     return render(request,'login/login.html')
     
def login_volunteer(request):
    return render(request,'login//volunteer-login/volunteer.html')
    

def login_victim(request):
    return render(request,'login/victim_login.html')

def login_ngo(request):
    return render(request,'login/ngo_login.html')
def home(request):
    return render (request, 'login/home.html')     