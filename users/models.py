from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser): #our CustomUser is the dublicate of AbstractUser means default user model
	age = models.PositiveIntegerField(default=0)
      