from django.shortcuts import render

def farmer(request):
    return render(request,'farmer.html')

def add_crop(request):
    return render(request,'add_crop.html')

def edit_crop(request):
    return render(request,'edit_crop.html')

def trader(request):
    return render(request,'trader_home.html')

def trader_buy_crop(request):
    return render(request,'trader_buy_crop.html')

def purchases(request):
    return render(request,'trader_purchases.html')
