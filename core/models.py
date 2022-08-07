from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=255)
    bio = models.TextField()
    zipCode = models.PositiveIntegerField(default=0)
    imageUrl = models.ImageField(upload_to='profile', default='')

