from django.shortcuts import render,redirect
from .models import Trader,Farmer
from django.contrib import messages
import bcrypt   


def home_page(request):
    return render(request,"Home_page.html")

def login_page(request):
    return render(request,"login.html")    

def register(request):
    if request.POST['user_type'] =='farmer': 
        errors = Farmer.objects.register_validator(request.POST)
        request.session['coming_from']='REGISTER'
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')        
        else: 
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()   
                print(pw_hash)     
                this_farmer=Farmer.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                phone_number=request.POST['phone_number'],
                password=pw_hash)
                request.session['id']=this_farmer.id
                return redirect('/farmer')

    elif request.POST['user_type'] =='trader': 
        errors = Trader.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        else:     
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()   
            print(pw_hash)     
            this_trader=Trader.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            password=pw_hash)
            request.session['id']=this_trader.id
            return redirect('/trader')    


def login_proccese(request):
    if Farmer.objects.filter(email=request.POST['email']):
        request.session['coming_from']='LOGIN'
        errors = Farmer.objects.login_validator(request.POST)
        farmer = Farmer.objects.filter(email=request.POST['email'])
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        if  len(farmer)==0:
            messages.error(request, "invalid user")
            return redirect('/login')
        elif not (bcrypt.checkpw(request.POST['password'].encode(), farmer[0].password.encode())):
            messages.error(request, "invalid password")
            return redirect('/login')
        else:
            request.session['id']=farmer[0].id
            return redirect('/farmer')
    elif Trader.objects.filter(email=request.POST['email']):
        request.session['coming_from']='LOGIN'
        errors = Trader.objects.login_validator(request.POST)
        trader = Trader.objects.filter(email=request.POST['email'])
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        if  len(trader)==0:
            messages.error(request, "invalid user")
            return redirect('/login')
        elif not (bcrypt.checkpw(request.POST['password'].encode(), trader[0].password.encode())):
            messages.error(request, "invalid password")
            return redirect('/login')
        else:
            request.session['id']=trader[0].id
            return redirect('/trader')
    else:
        messages.error(request,"invalid email")
        return redirect('/login')   