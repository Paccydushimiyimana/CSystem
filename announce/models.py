from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title=models.CharField(max_length=100, unique=True)
    content = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.title

