from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.ChartField(max_length=100)
    age = models.IntegerField()
    usn = models.ChartField(max_length=100, unique=True)
    branch = models.ChartField(max_length=50)
    sem = models.IntegerField()
    course = models.ChartField(max_length=50)

def __str___(self):
    return self.name