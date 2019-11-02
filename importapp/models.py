from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    RollNo = models.IntegerField()
    Phone = models.IntegerField()
    Topic = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
