from rest_framework.serializers import ModelSerializer
from appone.models import *

class placeSerializer(ModelSerializer):
    class Meta:
        Model = place
        fields = '__all__'

class CollegeSerializer(ModelSerializer):
    class Meta:
        Model = College
        fields = '__all__'


class SubjectSerializer(ModelSerializer):
    class Meta:
        Model = Subject
        fields = '__all__'

class DepartmentSerializer(ModelSerializer):
    class Meta:
        Model = Department
        fields = '__all__'
        
