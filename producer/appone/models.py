from django.db import models

# Create your models here.

class place(models.Model):
    Name = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40)
    pincode = models.IntegerField()

class College(models.Model):
    ClgName = models.CharField(max_length = 40)
    ClgOwner = models.CharField(max_length = 40)
    ClgPlace = models.OneToOneField(place, on_delete = models.CASCADE, primary_key = True)

class Subject(models.Model):
    SubName = models.CharField(max_length = 40)
    SubCode = models.IntegerField()
    SubCollege = models.ManyToManyField(College)

class Department(models.Model):
    DeptName = models.CharField(max_length = 40)
    DeptCode = models.IntegerField()
    DeptSubject = models.ForeignKey(Subject, on_delete = models.CASCADE)
