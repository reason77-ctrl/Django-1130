from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length= 300)
    email = models.CharField(max_length= 300)
    subject = models.TextField()
    message = models.TextField()