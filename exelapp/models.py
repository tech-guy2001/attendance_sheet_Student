from django.db import models

# Create your models here.
# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    marks = models.IntegerField()



class Students(models.Model):
    BATCH_CHOICES = [
        ('morning', 'Morning Batch'),
        ('afternoon', 'Afternoon Batch'),
        ('evening', 'Evening Batch'),
        ('weekend', 'Weekend Batch'),
    ]

    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,null=True)
    join_date = models.DateField()
    contact_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    batch = models.CharField(max_length=20, choices=BATCH_CHOICES)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class  attendance(models.Model):
    name = models.CharField(max_length=100,null=True)
    dates= models.DateField()
    intime= models.CharField(max_length=100,null=True)
    outtime=models.CharField(max_length=100,null=True)
    staff=models.CharField(max_length=100,null=True)
    topic=models.CharField(max_length=100 ,null=True)
    email=models.CharField(max_length=100 ,null=True)



