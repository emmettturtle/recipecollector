from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=300)
    directions = models.TextField(max_length=500)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})
    
    def avg_rating(self):
        total_rating = 0
        for comment in self.comment_set.all():
            total_rating += comment.rating
        avg = total_rating/self.comment_set.all().count()
        return avg
        
    

class Comment(models.Model):
    date = models.DateField()
    rating = models.IntegerField()
    comment = models.TextField(max_length=300)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment} on {self.date}"
    
    class Meta:
        ordering = ['-date']


