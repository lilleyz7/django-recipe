from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    name = models.CharField(max_length=40)
    steps = models.TextField(help_text="List each step on a new line."  )
    ingredients = models.TextField(help_text="List each ingredient on a new line.")
    tag = models.CharField(max_length=20, default="none")

    def __str__(self):
        return self.name
