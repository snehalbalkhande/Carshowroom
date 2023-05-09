from django.shortcuts import render, redirect, HttpResponse
from .models import Car, Contact
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from math import ceil

# Create your views here.

def index(request):
    Cars= Car.objects.all()
    allCars=[]
    carprods= Car.objects.values('car_type', 'id')
    cars= {item["car_type"] for item in carprods}
    for car in cars:
        ca=Car.objects.filter(car_type=car)
        n = len(ca)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allCars.append([ca, range(1, nSlides), nSlides])

    params={'allCars':allCars }
    return render(request,"home/index.html", params)


def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'home/contact.html')




def carview(request, carid):
    
   car=Car.objects.filter(id=carid)
   
   return render(request, 'home/carview.html',{'cardesc':car[0]})  



def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect("/home")

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/home")

    return HttpResponse("404- Not found")
   


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("/home")
    #return render(request,"home/index.html")

