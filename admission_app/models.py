from pickle import TRUE
from django.db import models
import re

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_pw']:
                errors['password'] = "Passwords DO NOT match!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')   
        if not postData["email"]:
                errors["email"] = "Please enter email (Empty Check)"
        elif not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"     
        try:
            email_exist=User.objects.get(email=postData["email"])
            if email_exist : # there is user already with this email 
                errors["email"] = "The email is already exist, please try another one"
        except:
            pass
        
        return errors
    
    def file_validatior(self,file):
        limit = 2 * 1024 * 1024
        errors={}
        if not file.name.endswith((".pdf")):
            errors['ext']="Only PDF files are accepted"
        if file.size > limit:
            errors['file_size']='File too large. Size should not exceed 2 MiB.'
        return errors

class CourseManager(models.Manager):
    def basic_validator_files(self,postData):
        errors={}
        
        if not postData['photo'].name.endswith((".jpg",".png",".gif",".jpeg")):
            errors['img']="Only images end with .png, .gif, .jpg and .jpeg are accepted"
        return errors
    
    def basic_validator(self,postData):
        errors={}
        if len(postData['desc']) > 200:
            errors['desc'] = "The length of Description is should be less than 200 characters"
        
        return errors
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc=models.TextField()
    photo = models.ImageField(upload_to='images/', null=True)
    capacity=models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=CourseManager()

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    role = models.CharField(max_length=255) #student or manager.
    course = models.ForeignKey(Course, related_name="users", on_delete=models.CASCADE, null=True)
    state = models.CharField(null= True, max_length=255)
    password = models.CharField(max_length=255)
    cv = models.FileField(upload_to='cv_files/',null=True, default='Empty')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= userManager()

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message=models.TextField()
    read = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

