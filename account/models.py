from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='+')
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    slug = models.SlugField()
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='images/', default = "text.jpg")
    

    

class Form(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField( max_length=50)




