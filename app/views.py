from django.shortcuts import render

from .serializers import StudentSerilizer
from .models import Student
from rest_framework import viewsets
# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerilizer