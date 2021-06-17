from django.db import models
from rest_framework import fields, serializers

# Create your models here.
class Employee(models.Model):
    full_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    contact=models.CharField(max_length=20)
    address=models.TextField()


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields="__all__"
