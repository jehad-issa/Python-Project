from django.shortcuts import render
	
import sys
print(sys.getrecursionlimit())

def farmer(request):
    return render(request,'farmer.html')

def add_crop(request):
    return render(request,'add_crop.html')

def edit_crop(request):
    return render(request,'edit_crop.html')

def sales(request):
    return render(request,'sales.html')
