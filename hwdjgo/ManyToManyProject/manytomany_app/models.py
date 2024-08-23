from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=30)
    age = models.IntegerField()
    courses = models.ManyToManyField('Course', on_delete=models.CASCADE)

class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    students = models.ManyToManyField(Student, on_delete=models.CASCADE)