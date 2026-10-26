
from rest_framework import serializers
from .models import StudentDb

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDb
        fields = '__all__'
