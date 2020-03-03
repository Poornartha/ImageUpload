from django.db import models

# Create your models here.
# models.py


class Hotel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    hotel_Main_Img = models.ImageField(upload_to='images/', null=True, blank=True)
