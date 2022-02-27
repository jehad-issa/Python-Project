from django.shortcuts import redirect, render
from login_app.models import Trader,Farmer,Crop,Sale
from django.contrib import messages


def farmer(request):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        this_farmer=Farmer.objects.get(id=request.session['id'])
        
        context={
            'this_farmer':this_farmer,
            'sales':this_farmer.sales.all(),
            
        }
        return render(request,'farmer.html',context)

def add_crop(request):
    this_farmer=Farmer.objects.get(id=request.session['id'])
    cont={
        'this_farmer':this_farmer
    }
    return render(request,'add_crop.html',cont)

def new_crop(request):
    errors = Crop.objects.add_crop_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/farmer/add_crop')
    else:
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
    errors = Crop.objects.add_crop_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/farmer/edit_crop/{num}')
    else:
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
    if 'id' not in request.session:
        return redirect('/login')
    this_trader=Trader.objects.get(id=request.session['id'])
    context={
        'crops_single':Crop.objects.values('crop_name').order_by('crop_name').distinct,
        'crops':Crop.objects.all(),
        'trader':Trader.objects.get(id=request.session['id'])
    }
    return render(request,'trader.html',context)

def trader_buy_crop(request ,crop_id):
    context={
        'this_crop':Crop.objects.get(id=crop_id)
    }
    return render(request,'trader_buy_crop.html' ,context)

def buy(request,crop_id):
    this_crop=Crop.objects.get(id=crop_id)
    if this_crop.sales.all():
        this_sale=this_crop.sales.all()[0]
        new_quantity=this_sale.quantity + int(request.POST['quantity'])
        this_sale.quantity=new_quantity
        this_sale.save()
        this_crop.quantity=this_crop.quantity - int(request.POST['quantity'])
        this_crop.save()
        print(new_quantity)
        return redirect(f'/trader/{crop_id}')
    else:
        new_quantity=int(request.POST['quantity'])
        Sale.objects.create(crop=Crop.objects.get(id=crop_id),
        trader=Trader.objects.get(id=request.session['id']),
        farmer=this_crop.farmer,
        quantity=new_quantity)
        this_crop.quantity=this_crop.quantity - new_quantity
        this_crop.save()
        return redirect(f'/trader/{crop_id}')


def purchases(request):
    this_trader=Trader.objects.get(id=request.session['id'])
    context={
        'sales':this_trader.sales.all(),
    }
    return render(request,'trader_purchases.html',context)

def logout(request):
    del request.session['id']
    return redirect('/login')
