from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from demoproject.form import Loginform

# Create your views here.
def Login(request):
    if request.method == "POST":
        form = Loginform(request.POST)
        form = Loginform(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                    login(request,user)
                    return redirect('Home')
            else:
                    messages.info(request, 'LOGIN  FAILED')
                    return render(request, 'pages-login.html',{'form' : form})
        else:
                messages.info(request, 'LOGIN  FAILED')
                return render(request, 'pages-login.html',{'form' : form}) 
    else:    
        form = Loginform()
        return render(request, 'pages-login.html',{'form' : form})
def Home(request):
    return render(request, 'index5.html')