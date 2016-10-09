from django.contrib import admin

# Register your models here.
from .models import Author, ComicBook, Review

admin.site.register(Author)
admin.site.register(ComicBook)
admin.site.register(Review)