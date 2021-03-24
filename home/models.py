from django.db import models

# Create your models here.
CATEGORY = (
    ('vector', 'vector'),
    ('raster', 'raster'),
    ('ui', 'ui'),
    ('printing', 'printing')
)
STATUS = (
    ('active', 'active'),
    ('', 'default')
)

class Contact(models.Model):
    name = models.CharField(max_length= 300)
    email = models.CharField(max_length= 300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length= 300)
    profession = models.CharField(max_length= 300, blank= True)
    images = models.TextField()
    comment = models.TextField()
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length= 300)
    images = models.TextField()
    discription = models.CharField(max_length= 300)
    category = models.CharField(choices= CATEGORY, blank= True, max_length= 100)
    status = models.CharField(choices= STATUS, blank= True, max_length= 100)
    def __str__(self):
        return self.name

class Brand(models.Model):
    title = models.CharField(max_length=100, blank= True)
    images = models.TextField()
    def __str__(self):
        return self.title