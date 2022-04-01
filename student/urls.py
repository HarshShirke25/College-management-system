from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path("dashboard",views.dashboard,name="dashboard_std"),
    path("attendance",views.attendance,name="attendance_stu"),
    path("UTMarks",views.UTMarks,name="UTMarks_stu"),
    path("profile",views.profile,name="profile"),
    path("schedule",views.schedule,name="schedule"),
    
    
]
