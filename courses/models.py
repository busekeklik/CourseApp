from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(default="", null=False, unique=True, db_index=True, max_length=50)
    courses = models.ManyToManyField(Course, related_name="categories")
    
    def __str__(self):
        return f"{self.title} {self.date}"

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, unique=True, db_index=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title} {self.date}"


