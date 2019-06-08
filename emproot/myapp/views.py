from django.shortcuts import render
from .models import Employee
from rest_framework.viewsets import ModelViewSet
from .serializers import EmployeeSerializers


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
# Create your views here.
