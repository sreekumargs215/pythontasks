
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class Person(models.Model):
  
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  email = models.EmailField()
  date = models.DateTimeField()


class loginperson(models.Model):
  email=models.CharField()
  password=models.CharField()

#   phone = models.IntegerField(null=True)
#   joined_date = models.DateField(null=True)

#   def __str__(self):
#     return f"{self.firsname} {self.lastname}"