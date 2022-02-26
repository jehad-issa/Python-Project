from tkinter import CASCADE
from urllib import request
from django.db import models

class Farmer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone_number=models.IntegerField()
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Trader(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone_number=models.IntegerField()
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Crop(models.Model):
    crop_name=models.CharField(max_length=255)
    quantity=models.IntegerField()
    quality=models.CharField(max_length=3)
    price=models.IntegerField()
    desc=models.TextField()
    farmer=models.ForeignKey(Farmer,related_name='crops',on_delete=CASCADE)
    traders=models.ManyToManyField(Trader,through='Sale')

class Sale(models.Model):
    crop=models.ForeignKey(Crop,on_delete=CASCADE)
    trader=models.ForeignKey(Trader,on_delete=CASCADE)
    quantity=models.IntegerField()