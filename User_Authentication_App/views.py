from django.shortcuts import render
from django.contrib.auth.models import User
from User_Authentication_App.forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home_view(request):
    context = {
        "user" : request.user
    }
    return render(request,'home.html',context)


def RegisterView(request):
    if request.method=='POST':
        pass
    else:
        form = RegisterForm()
        return render(request,'register.html',{'form':form})

    