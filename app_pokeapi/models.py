from django.contrib.auth.models import AbstractBaseUser
from django.db import models

<<<<<<< HEAD
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
=======

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
>>>>>>> main
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username