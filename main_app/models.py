from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=300)
    directions = models.TextField(max_length=500)

    