from django.db import models
from django.core import validators

# Create your models here.

class Student(models.Model):
    student_id=models.IntegerField(primary_key=True)
    student_name=models.CharField(max_length=100,validators=[validators.MinLengthValidator(5)])
    student_age=models.IntegerField()
    student_phno=models.IntegerField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    email=models.EmailField()

    def __str__(self):
        return str(self.student_name)