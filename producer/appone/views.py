from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from appone.models import *
from .serializers import *

class placeOp(ModelViewSet):
    queryset = place.objects.all()
    serializer_class = placeSerializer()


class collegeOp(ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer()


class subjectOp(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer()


class deptOp(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer()



# Create your views here.

