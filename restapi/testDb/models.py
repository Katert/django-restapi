from django.db import models


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100)


class Role(models.Model):
    title = models.CharField(max_length=20)
    salary_scale = models.IntegerField()
