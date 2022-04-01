from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User,Group
from .utils import have_group
# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request,"authapp/login.html")
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password:
            user = auth.authenticate(username=username,password=password)
            if user:
                if have_group(user,"STUDENT"):
                    auth.login(request,user)
                    return redirect('dashboard_std')
                elif have_group(user,"USER"):
                    auth.login(request,user)
                    return redirect('dashboard_tch')
        else:
            return render(request,"authapp/login.html")
                  
    return render(request,"authapp/login.html")

def register_std(request):
    if request.method == "GET":
        return render(request,"authapp/reg_std.html")
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['psw-repeat']

        user = User.objects.create_user(username,email,password)
        user.firstname = firstname
        user.lastname = lastname
        my_group = Group.objects.get_or_create(name="STUDENT")
        my_group[0].user_set.add(user)
        user.save()

        return render(request,"student/dashboard.html")

    return render(request,"authapp/reg_std.html")

def register_tch(request):
    if request.method == "GET":
        return render(request,"authapp/reg_tch.html")
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['psw-repeat']

        user = User.objects.create_user(username,email,password)
        user.firstname = firstname
        user.lastname = lastname
        my_group = Group.objects.get_or_create(name="TEACHER")
        my_group[0].user_set.add(user)
        user.save()

        return render(request,"teacher/dashboard.html")

    
    return render(request,"authapp/reg_tch.html")