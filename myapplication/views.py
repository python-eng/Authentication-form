from django import http
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from myapplication.models import Singup
from myapplication.forms import SignUpForm,LoginForm,UpdateForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.


def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Your account has been secussfully created')
                return redirect('/')
    else:
        redirect('/dashboard/')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                username=fm.cleaned_data['username']
                password=fm.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'You have successfully login')
                    return redirect('/dashboard/')
        else:
            fm=LoginForm()
            signup=SignUpForm()
    else:
        return redirect('/dashboard/')
    
    return render(request,'myapplication/index.html',{'form':fm,'signupform':signup})


def dashboard(request):
    fm=UpdateForm()
    alluser=Singup.objects.all()
    return render(request,'myapplication/dashboard.html',{'user':alluser,'form':fm})


def userupdate(request,id):
    if request.method=='POST':
        obj=Singup.objects.get(pk=id)
        fm=UpdateForm(request.POST,instance=obj)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Your record has been secussfully updated')
            return redirect('/dashboard/')
    else:
        obj=Singup.objects.get(pk=id)
        fm=UpdateForm(instance=obj)
    return render(request,'myapplication/update.html',{'form':fm})

def user_logout(request):
    logout(request)
    return redirect('/')

def user_delete(request,id):
    if request.method=='POST':
        obj=Singup.objects.get(pk=id)
        obj.delete()
        return redirect('/dashboard/')





