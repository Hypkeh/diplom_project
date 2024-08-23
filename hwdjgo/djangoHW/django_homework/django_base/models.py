from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    name = models.CharField(max_length=40)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    

class Order(models.Model):
    location = models.CharField(max_length=20)

class Electronics(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Clothing(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    price = models.PositiveIntegerField()   
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Books(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
