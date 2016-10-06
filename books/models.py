from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class ComicBook(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add=True)