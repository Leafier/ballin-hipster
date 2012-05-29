from django.db import models

# Create your models here.
class Category(models.Model):
    keyname = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    tagline = models.CharField(max_length=50)
    desc = models.TextField(max_length=400)
    pub_date = models.DateTimeField('Date Published')
    color = models.CharField(max_length=7)

class Artifact(models.Model):
    keyname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    tagline = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    desc = models.TextField(max_length=1000)
    image = models.FileField(upload_to='images/')
    example = models.URLField(max_length=100)
    exampletoggle = models.BooleanField()
    tech = models.CharField(max_length=500)
