from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'register.html',{})


def login(request):
    return render(request,'login.html',{})


def createProfile(request):
    return render(request,'create-profile.html',{})



def viewProfile(request):
    return render(request,'view-profile.html',{})