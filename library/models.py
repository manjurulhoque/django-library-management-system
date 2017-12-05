from django.db import models
from datetime import date


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    categories = models.ManyToManyField(Category)
    cover = models.TextField(max_length=100000, blank=True, null=True)
    author = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=25000, blank=True, null=True)
    available = models.IntegerField(default=0)


class Student(models.Model):
    student_id = models.CharField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    section = models.CharField(max_length=10)
    year = models.CharField(max_length=10)


class Borrow(models.Model):
    book = models.ManyToManyField(Book)
    student = models.ManyToManyField(Student)
    qty = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=25)
