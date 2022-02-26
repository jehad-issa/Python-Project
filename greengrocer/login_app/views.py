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
                Farmer.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                phone_num=request.POST['phone_num'],
                password=pw_hash)
                # messages.success(request, "User successfully create")
                # if 'first_name' not in request.session:
                #     request.session['first_name']=request.POST['first_name']
                return redirect('/home')

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
            Trader.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone_num=request.POST['phone_num'],
            password=pw_hash)
            # messages.success(request, "User successfully create")
            # if 'first_name' not in request.session:
            #     request.session['first_name']=request.POST['first_name']
            return redirect('/home')    


def login_proccese(request):
    if Farmer.objects.filter(email=request.POST['email']):
        errors = Farmer.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        else:
            errors = Farmer.objects.login_validator(request.POST)
        request.session['coming_from']='LOGIN'
        farmer = Farmer.objects.filter(email=request.POST['email'])
        print(farmer)
        if (len(farmer)>0): 
            logged_farmer = Farmer.objects.get(email=request.POST['email'])
        
            if bcrypt.checkpw(request.POST['password'].encode(), logged_farmer.password.encode()):
                # messages.success(request,"user seccessfuly lonin")
                if 'first_name' not in request.session:
                    request.session['first_name']=farmer[0].first_name
                    print(request.session['first_name'])
        return redirect('/home')
    elif Trader.objects.filter(email=request.POST['email']):
        errors = Trader.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        else:
            errors = Trader.objects.login_validator(request.POST)
        # request.session['coming_from']='LOGIN'
        trader = Trader.objects.filter(email=request.POST['email'])
        print(trader)
        if (len(trader)>0): 
            logged_trader = Trader.objects.get(email=request.POST['email'])
        
            if bcrypt.checkpw(request.POST['password'].encode(), logged_trader.password.encode()):
                # messages.success(request,"user seccessfuly lonin")
                if 'first_name' not in request.session:
                    request.session['first_name']=farmer[0].first_name
                    print(request.session['first_name'])
        return redirect('/home')
    else:
        messages.error(request,"invalid email")
        return redirect('/login')   