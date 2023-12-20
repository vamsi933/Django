from django.db import models

# Create your models here.
class Iplmatches(models.Model):
    name= models.CharField(max_length = 100)
    Headcoach=models.CharField(max_length=100)
    captain = models.CharField(max_length= 100)
    no_of_Trophies= models.IntegerField()
    
