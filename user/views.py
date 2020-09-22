from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Profile

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
        if request.method == "POST":
                firstname = request.POST['fname']
                lastname = request.POST['lname']
                sex = request.POST['sex']
                dob_day = request.POST['day']
                dob_month = request.POST['month']
                dob_year = request.POST['year']
                religion = request.POST['religion']
                caste = request.POST['caste']
                subcaste = request.POST['subcaste']
                country = request.POST['country']
                state = request.POST['state']
                district = request.POST['district']
                age = request.POST['age']
                maritalstatus = request.POST['maritalstatus']
                profileby = request.POST['profileby']
                education = request.POST['education']
                edudescr = request.POST['edudescr']
                bodytype = request.POST['bodytype']
                physicalstatus = request.POST['physicalstatus']
                drink = request.POST['drink']
                smoke = request.POST['smoke']
                mothertounge = request.POST['mothertounge']
                bloodgroup = request.POST['bloodgroup']
                weight = request.POST['weight']
                height = request.POST['height']
                colour = request.POST['colour']
                diet = request.POST['diet']
                occupation = request.POST['occupation']
                occupationdescr = request.POST['occupationdescr']
                income = request.POST['income']
                fatheroccupation = request.POST['fatheroccupation']
                motheroccupation = request.POST['motheroccupation']
                sis = request.POST['sis']
                bros = request.POST['bros']
                aboutme = request.POST['aboutme']
                
                
                profile = Profile(user=request.user,firstname=firstname,lastname=lastname,sex=sex,dob_day=dob_day,dob_month=dob_month,dob_year=dob_year,religion=religion,caste=caste,subcaste=subcaste,country=country,state=state,district=district,age=age,maritalstatus=maritalstatus,profileby=profileby,education=education,specialization=edudescr,bodytype=bodytype,physicalstatus=physicalstatus,drink=drink,smoke=smoke,mothertounge=mothertounge,bloodgroup=bloodgroup,weight=weight,height=height,colour=colour,diet=diet,occupation=occupation,occupationdescr=occupationdescr,income=income,fatheroccupation=fatheroccupation,motheroccupation=motheroccupation,sis=sis,bros=bros,aboutme=aboutme)
                profile.save()
                messages.info(request,"Profile saved!!!")
                return redirect('view-profile')
                
                        
	        


        else:
                return render(request,'create-profile.html',{})


@login_required(login_url='/user/login/')
def viewProfile(request):
    return render(request,'view-profile.html',{})



def logout(request):
    auth.logout(request)
    return redirect('user-login')