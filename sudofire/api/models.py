from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)


class Customer(models.Model):
    profile_number = models.OneToOneField(User, on_delete=models.CASCADE)
    