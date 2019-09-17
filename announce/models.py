from django.db import models
from django.contrib.auth.models import User

# class Student(models.Model):
#     firstname = models.TextField(max_length=200)
#     lastname = models.TextField(max_length=200)
#     email = models.EmailField(max_length=200)
#     phone = models.IntegerField(max_length=200)
#     stdtype = models.ForeignKey(Topic, related_name='posts')
#     regnumber = models.DateTimeField(auto_now_add=True) 
#     level = models.DateTimeField(null=True)
#     school = models.ForeignKey(School, related_name='name')
#     department = models.ForeignKey(Department, related_name='name')
