from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import destination

# Create your views here.
def index(request):
    dests = destination.objects.all()
    return render(request, 'index.html',{'dests':dests})




def home(request):

    return render(request, 'index.html')


