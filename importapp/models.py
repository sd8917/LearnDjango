from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    rollno = models.IntegerField(default=1) #Note here the Primat key make this fi
    phone = models.IntegerField()
    topic = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
