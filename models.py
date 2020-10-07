from django.db import models

# Create your models here.

class Studentmaster(models.Model):

    sname = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=200)
    address = models.TextField(max_length=500)
    mno = models.BigIntegerField()
