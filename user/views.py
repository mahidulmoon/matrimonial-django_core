from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        username=request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['fname']
        lastname = request.POST['lname'] 

        if User.objects.filter(username=username).exists():
                messages.info(request,"Username Token!!!")
                return render(request,'register.html')
        elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Token!!!")
                return render(request,'register.html')
        else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save()  
                messages.warning(request, "Registration Completed!!!")
                return render(request,'register.html') 
    else:
        return render(request,'register.html')

    


def login(request):
    return render(request,'login.html',{})


def createProfile(request):
    return render(request,'create-profile.html',{})



def viewProfile(request):
    return render(request,'view-profile.html',{})