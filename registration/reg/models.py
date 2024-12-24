from django.db import models
from django.contrib.auth.models import User
from reg import *


class Registration(models.Model):
   user_name = models.CharField(max_length=100,null=True)
   ph_number = models.IntegerField(null=True)
   password = models.CharField(max_length=100,null=True)
   email = models.EmailField(null=True)

   def __str__(self):
        return self.user_name

class Ontimepassword(models.Model):
   otp_number = models.IntegerField(null=True)
   email = models.EmailField(null=True)
   user_name = models.CharField(max_length=100,null=True)
   ph_number = models.IntegerField(null=True)
   password = models.CharField(max_length=100,null=True)
   


# Create your models here.
