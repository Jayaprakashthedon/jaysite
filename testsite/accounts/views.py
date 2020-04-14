from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Already Exists')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save();
                messages.info(request,'User Created')
        else:
            messages.info(request,'Password does not match')
        return redirect('/travello/accounts/signup')
    else:
        return render(request, 'signup.html')
# Create your views here.
