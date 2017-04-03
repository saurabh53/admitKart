from __future__ import unicode_literals

from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    rank = models.IntegerField()
    year_of_establishment = models.IntegerField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    fees = models.DecimalField(max_digits=20,decimal_places=2)
    duration= models.DecimalField(max_digits=20,decimal_places=2)
    university = models.ForeignKey(University,related_name='course')

