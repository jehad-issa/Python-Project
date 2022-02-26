from django.db import models
import re
from multiprocessing import Manager


class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors["first_name"] = "User first-nmae should be at least 3 characters"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "User last-name should be at least 3 characters"
        # if len(postData['email']) < 4:
        #     errors["email"] = "Blog email should be at least 4 characters" 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address!"
        if len (Farmer.objects.filter(email=postData['email']))==1:
            errors['exsistance']="this email already exisit"
        elif len (Trader.objects.filter(email=postData['email']))==1 :
            errors['exsistance']="this email already exisit"

        if len(postData['phone_num']) < 14:
            errors["last_name"] = "User phone-number should be start with(00972)"
        if postData['password'] != postData['conf_password']:
            errors['matching_pass'] = "the given password do not match"      
        if len(postData['password']) < 6:
            errors["password"] = "User password should be at least 6 characters"
        if len(postData['conf_password']) < 6:
            errors["conf_password"] = "User conf_password should be at least 6 characters"         
        return errors


    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 6:
            errors["password"] = "User password not correct"    
        return errors



class Trader(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_num= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Farmer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_num= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()    