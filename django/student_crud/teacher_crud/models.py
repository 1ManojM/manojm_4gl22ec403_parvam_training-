from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=50)
    quallification = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    experience = models.IntegerField()

def __str___(self):
    return self.name