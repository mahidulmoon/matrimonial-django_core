from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

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
                return redirect('user-register') 
    else:
        return render(request,'register.html')

    


def login(request):
    if request.method == "POST":
            username=request.POST['username']
            password=request.POST['password']

            user=auth.authenticate(username=username,password=password)
            if user is not None:
                    auth.login(request,user)
                    return redirect('view-profile')
            else:
                    messages.info(request,"Invalid Username and Password")
                    return render(request,'login.html')
    else:
        return render(request,'login.html',{})
    

@login_required(login_url='/user/login/')
def createProfile(request):
    return render(request,'create-profile.html',{})


@login_required(login_url='/user/login/')
def viewProfile(request):
    return render(request,'view-profile.html',{})



def logout(request):
    auth.logout(request)
    return redirect('user-login')