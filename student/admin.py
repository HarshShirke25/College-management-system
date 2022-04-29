from distutils.command.config import config
from django.contrib import admin
from .models import Student

# Register your models here.

admin.site.register(Student)
