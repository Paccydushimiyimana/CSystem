from django.db import models

from django.contrib.auth.models import User


class College(models.Model):
    name=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
class School(models.Model):
    name=models.CharField(max_length=20, unique=True)
    college=models.ForeignKey(College, related_name='schools', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=30, unique=True)
    school=models.ForeignKey(School, related_name='departments',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    name=models.IntegerField()  
    department=models.ForeignKey(Department, related_name='levels', on_delete=models.SET_NULL, null=True)      

    
