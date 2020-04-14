from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")


def hai(request):
    return render(request,'hai.html',{'name':'JAY'})


def add(request):
    val1 = int(request.POST['Num1'])
    val2 = int(request.POST['Num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result':res})
