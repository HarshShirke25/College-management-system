from operator import mod
from django.db import models
from django.forms import CharField

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    Class = models.CharField(max_length = 30)
    branch = models.CharField(max_length=30)
    grno = models.IntegerField()
    birth = models.DateField(max_length=30)
    address = models.TextField(max_length=100)
    bloodgroup = models.CharField(max_length=10)

    def __str__(self):
        return self.name

