
from django.shortcuts import render

# Create your views here.

def dashboard(request):
    if request.method == "GET":
        return render(request,"teacher/dashboard.html")


def stdattendance(request):
    if request.method == "GET":
        return render(request,"teacher/studentattendance.html")

def timetable(request):
    if request.method == "GET":
        return render(request,"teacher/teachertt.html")

def teacherprofile(request):
    if request.method == "GET":
        return render(request,"teacher/teacherprofile.html")
