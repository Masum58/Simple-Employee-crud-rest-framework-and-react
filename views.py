from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee,EmployeeSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all().order_by('id')
