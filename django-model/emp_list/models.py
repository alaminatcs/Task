from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length= 20)
    id = models.IntegerField(primary_key= True)
    address = models.TextField()