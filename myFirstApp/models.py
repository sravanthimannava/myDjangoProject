from django.db import models

# Create your models here.
class Vehicle(models.Model):
    title = models.CharField(max_length = 200,unique=True)
    types = models.CharField(max_length = 10)
    description = models.TextField()

    def __str__(self):
        return self.title

class Sales(models.Model):
    name = models.ForeignKey(Vehicle,on_delete=models.DO_NOTHING,)
    company = models.CharField(max_length = 128)
    year = models.CharField(max_length = 4)

    def __str__(self):
        return self.name
