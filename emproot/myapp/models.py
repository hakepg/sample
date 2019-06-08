from django.db import models



#sub1 = Subject(SubName = 'ML', SubCode = 54367)


    
# stud1 = Student(StudName = 'Pratima',StudAge= 24)
class Place(models.Model):
    city= models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()

class College(models.Model):
    ColName = models.CharField(max_length=40)
    ColCode = models.FloatField()
    Place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)

'''
class Department(models.Model):
    DeptName = models.CharField(max_length = 40)
    DeptCode = models.FloatField()
    
# dept1 = Department(DeptName = 'CSE', DeptCode = 56467 )

class Student(models.Model):
    StudName = models.CharField(max_length=30)
    StudAge = models.IntegerField()
    College = models.ForeignKey(College, on_delete=models.CASCADE)

class Subject(models.Model):
    SubName = models.CharField(max_length = 40)
    SubCode = models.FloatField()
    Student = models.ManyToManyField(Student)
'''
    
# colg1 = College(ColName = 'Walchand', ColCode = 55767 )

    

# Create your models here.
