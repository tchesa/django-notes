from django.db import models

# Create your models here.

class Note(models.Model):
  slug = models.SlugField()
  title = models.TextField(unique=True)
  content = models.TextField(null=True, blank=True)
