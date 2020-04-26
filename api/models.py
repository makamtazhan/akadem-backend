from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=255)
class Major(models.Model):
    name = models.CharField(max_length=255)

class Manager(models.Model):
    name = models.CharField(max_length=255)

class Program(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255) 
    text = models.CharField(max_length=255)
    requirements = models.CharField(max_length=2048)

