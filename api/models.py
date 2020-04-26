from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=255)
class Major(models.Model):
    name = models.CharField(max_length=255)

