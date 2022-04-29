
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path("dashboard",views.dashboard,name="dashboard_tch"),
    path("stdattendance",views.stdattendance,name="stdattendance"),
    path("teachertt",views.timetable,name="teachertt"),
    path("teacherprofile",views.teacherprofile,name="teacherprofile"),

]