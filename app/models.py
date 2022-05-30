from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,blank=True)
    email=models.EmailField(max_length=100,blank=True)
    phone=models.IntegerField(blank=True)
    anser=models.CharField(max_length=100,blank=True)
    description=models.TextField(blank=True)