from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    profile_pic = models.ImageField(null=True, blank=True)
    email_id = models.CharField(max_length=20)
    address_line = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    profile_pic = models.ImageField(null=True, blank=True)
    email_id = models.CharField(max_length=20)
    address_line = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)



