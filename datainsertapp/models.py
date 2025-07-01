from django.db import models

# Create your models here.
class Data(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Address = models.CharField(max_length=100)
    
