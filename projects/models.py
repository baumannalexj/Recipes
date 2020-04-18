from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=1000)
    image = models.FilePathField(path="/img")

# Create your models here.
