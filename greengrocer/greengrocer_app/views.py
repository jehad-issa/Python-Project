from django.shortcuts import redirect, render
from login_app.models import Trader,Farmer,Crop,Sale


def farmer(request):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        this_farmer=Farmer.objects.get(id=request.session['id'])
        context={
            'this_farmer':this_farmer,
        }
        return render(request,'farmer.html',context)

        

def add_crop(request):
    this_farmer=Farmer.objects.get(id=request.session['id'])
    cont={
        'this_farmer':this_farmer
    }
    return render(request,'add_crop.html',cont)

def new_crop(request):
    this_crop=Crop.objects.create(crop_name=request.POST['crop'],quantity=request.POST['quantity'],
    quality=request.POST['quality'],price=request.POST['price'],desc=request.POST['desc'],
    farmer=Farmer.objects.get(id=request.session['id']))
    return redirect('/farmer')

def edit_crop(request,num):
    this_crop=Crop.objects.get(id=num)
    cont2={
        'this_crop':this_crop
    }
    return render(request,'edit_crop.html',cont2)

def new_edit_crop(request,num):
    this_crop=Crop.objects.get(id=num)
    this_crop.crop_name=request.POST['crop']
    this_crop.quantity=request.POST['quantity']
    this_crop.quality=request.POST['quality']
    this_crop.price=request.POST['price']
    this_crop.desc=request.POST['desc']
    this_crop.save()
    return redirect('/farmer')

def delete(request,num):
    this_crop=Crop.objects.get(id=num)
    this_crop.delete()
    return redirect ('/farmer')

def trader(request):
    return render(request,'trader_home.html')

def trader_buy_crop(request):
    return render(request,'trader_buy_crop.html')

def purchases(request):
    return render(request,'trader_purchases.html')

def logout(request):
    del request.session['id']
    return redirect('/login')
