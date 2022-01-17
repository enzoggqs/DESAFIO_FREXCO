# models.py
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length=15)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.name