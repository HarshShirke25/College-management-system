from django.shortcuts import render
from . models import Student

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

    if request.method == "POST":
        name = request.POST['name']
        Class = request.POST['class']
        branch = request.POST['branch']
        grno = request.POST['grno']
        birth = request.POST['birth']
        address = request.POST['address']
        bloodgroup = request.POST['bloodgroup']

        student = Student(name = name,Class = Class, branch = branch,grno = grno, birth = birth,address = address,bloodgroup = bloodgroup)
        student.save()
        return render(request,"student/studentprofile.html",{
            'name':name,
            'Class':Class,
            'branch':branch,
            'grno' : grno,
            'birth' : birth,
            'address' : address,
            'bloodgroup' : bloodgroup
        })

def schedule(request):
    if request.method == "GET":
        return render(request,"student/schedule.html")

