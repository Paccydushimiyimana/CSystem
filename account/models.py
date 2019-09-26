from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# class User(AbstractUser):
   
#     phone = models.IntegerField()
#     category = models.CharField(max_length=20)
#     student = models.CharField(max_length=20)
#     regNo=models.IntegerField()
#     lecturer = models.CharField(max_length=20)
#     staffId=models.IntegerField()
#     college_council = models.CharField(max_length=30)
#     academic_council = models.CharField(max_length=30)
#     school_council=models.CharField(max_length=30)
#     department_council=models.CharField(max_length=30)
#     school=models.CharField(max_length=30)
#     department=models.CharField(max_length=30)
#     level=models.CharField(max_length=30)
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name='profile', on_delete=models.SET_NULL, null=True)
#     phone = models.CharField(max_length=20)
#     category = models.CharField(max_length=20)
#     student = models.CharField(max_length=20, blank=True)
#     regNo=models.CharField(max_length=20,blank=True)
#     lecturer = models.CharField(max_length=20, blank=True)
#     staffId=models.CharField(max_length=20,blank=True)
#     college_council = models.CharField(max_length=30, blank=True)
#     academic_council = models.CharField(max_length=30, blank=True)
#     school_council=models.CharField(max_length=30, blank=True)
#     department_council=models.CharField(max_length=30, blank=True)
#     school=models.CharField(max_length=30, blank=True)
#     department=models.CharField(max_length=30, blank=True)
#     level=models.CharField(max_length=30, blank=True)
#     objects=models.UserManager()

# @receiver(post_save, sender=User)
# def profile_for_new_user(sender, instance , created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance).save()


class Category(models.Model):
    name=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Student_category(models.Model):
    name=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Lecturer_category(models.Model): 
    name=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name       

class College_council(models.Model):
    name=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class School_council(models.Model):
    name=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Department_council(models.Model):
    name=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name       

class Academic_council(models.Model):
    name=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name 

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
    name=models.CharField(max_length=1)  
    department=models.ForeignKey(Department, related_name='levels', on_delete=models.SET_NULL, null=True)      

    def __str__(self):
        return self.name

  
