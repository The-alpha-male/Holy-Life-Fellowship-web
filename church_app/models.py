import email
from email.mime import image
from pickletools import markobject

from django.db import models


# Create your models here.

class Contactus(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField(max_length=100) 

    def __str__(self):
        return self.full_name

class Gallery(models.Model):
    caption = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    thumbnail = models.ImageField(upload_to='gallery')
    created_date = models.DateTimeField(auto_now_add = True)
    
class Events(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=100)