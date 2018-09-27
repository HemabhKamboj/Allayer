from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def accounts(request):
    
    return render(request,'/accounts/profile.html')

# Create your views here.
