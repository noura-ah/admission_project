from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from admission_app.models import Course, User
from django.contrib import messages
import bcrypt
import os 
from django.conf import settings 
import matplotlib.pyplot as plt

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, errorMessage in errors.items():
                messages.error(request, errorMessage)
            return redirect("/")
        else:
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            phone= request.POST["phone"]
            password = request.POST["password"]
            passwordHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            newUser = User.objects.create(first_name=first_name,last_name=last_name,email=email,phone=phone,role = "Student",state="Pennding", password=passwordHash)
            request.session["userId"] = newUser.id
            messages.success(request, "User has been created")
            return redirect("/success")
    return render(request,"register.html") 

def login(request):
    if (User.objects.filter(email=request.POST['email']).exists()):
        user = User.objects.get(email=request.POST['email'])
        if (bcrypt.checkpw(request.POST['password'].encode(), user.password.encode())):
            request.session['userId'] = user.id
            if(user.role=="admin"):
               return redirect("/admin")
            else:   
               return redirect("/success")
    return redirect('/')

def dashboard(request):
    if "userId" not in request.session:
        return HttpResponse("Please authenticate first")

    user = User.objects.get(id=request.session["userId"])
    if(user.role=="Student"):
      context = {
        "user": user
      }
      return render(request, 'welcome.html', context)
    return HttpResponse("Please authenticate first")

def admin(request):
    if "userId" not in request.session:
        return HttpResponse("Please authenticate first")

    user = User.objects.get(id=request.session["userId"])
    course =Course.objects.get(id=6)
    if(user.role=="admin"):
      context = {
        "user": user,
        "course":course,
      }
      return render(request, 'admin.html', context)
    
    return HttpResponse("Please authenticate first")

def add_course(request):
    if request.method == "POST":
        name = request.POST["name"]
        desc = request.POST["desc"]
        photo = request.FILES["photo"]
        plt.savefig(os.path.join(settings.BASE_DIR, 'static\media\1.jpg'))
        course = Course.objects.create(name=name,desc=desc,photo=photo)
        return redirect("/admin") 
    return render(request,"add_course.html")

def logout(request):
    request.session.clear()
    messages.success(request, "You have been logged out!")
    return redirect("/")
    
# Hussein Solution:
# from django.core.files.base import ContentFile

# with open('/path/to/already/existing/file') as f:
#   data = f.read()


# Ahmed Solution:
# # obj.image is the ImageField
# obj.image.save('imgfilename.jpg', ContentFile(data))

# with open('path', 'wb+') as destination:
#         for chunk in request.FILES['photo'].chunks():
#             destination.write(chunk)

