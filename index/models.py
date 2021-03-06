# from _typeshed import Self
from pickle import TRUE
from django.db import models
from django.utils.text import slugify
from django.db.models.fields import CharField
# Create your models here.

class Trackin(models.Model):
    Tracking_ID = models.CharField(max_length=15, blank=True)
    Name = models.CharField(max_length=50, blank=True)
    Delivered = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(blank=True)
    Delivery_Date = models.CharField(max_length=20, blank=True)
    Delivery_Address = models.CharField(max_length=100, blank=True)
    Delivery_Country = models.CharField(max_length=50)
    Current_Location = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Tracking_ID)
        super(Trackin, self).save(*args, **kwargs)

    def __str__(self):
        return self.Tracking_ID
   

class Message(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    message = models.CharField(max_length=5000)

class Subscribe(models.Model):
    email = models.EmailField(max_length=100)
   
        