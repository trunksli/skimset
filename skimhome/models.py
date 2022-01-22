from django.db import models

# Create your models here

class SiteModel(models.Model):
	site = models.CharField(max_length=100)
	description = models.TextField()
	link = models.URLField(max_length=200)
	image = models.FilePathField(path="/img")