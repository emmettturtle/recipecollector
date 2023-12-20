from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=300)
    directions = models.TextField(max_length=500)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})