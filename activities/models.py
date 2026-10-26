from django.db import models

# Create your models here.
class StudentDb(models.Model):
    student_name=models.CharField(max_length=200)
    activity=models.CharField(max_length=200)
    hours=models.IntegerField()

    
    def __str__(self):
        return self.student_name

