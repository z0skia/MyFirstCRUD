from django.db import models

class Course(models.Model):

    name=models.CharField(max_length=40)
    commission = models.IntegerField()

class Student(models.Model):
    name= models.CharField(max_length=30)
    surname= models.CharField(max_length=30)
    email= models.EmailField()

class Teacher(models.Model):
    name= models.CharField(max_length=30)
    surname= models.CharField(max_length=30)
    email= models.EmailField()
    profession= models.CharField(max_length=30)

class Practice(models.Model):
    name= models.CharField(max_length=30)
    deliveryDate= models.DateField()
    delivered= models.BooleanField()

