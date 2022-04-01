from django.shortcuts import render

# Create your views here.

def dashboard(request):
    if request.method == "GET":
        return render(request,"student/dashboard.html")

def attendance(request):
    if request.method == "GET":
        return render(request,"student/attendance.html")

def UTMarks(request):
    if request.method == "GET":
        return render(request,"student/UTMarks.html")

def profile(request):
    if request.method == "GET":
        return render(request,"student/studentprofile.html")

def schedule(request):
    if request.method == "GET":
        return render(request,"student/schedule.html")

