from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path("register_std",views.register_std,name="register_std"),
    path("register_tch",views.register_tch,name="register_tch"),
]
