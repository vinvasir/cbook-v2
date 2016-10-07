from django import forms
from .models import ComicBook, Author

class ComicBookForm(forms.ModelForm):
    class Meta:
        model = ComicBook
        fields = ['title', 'description', 'author',]
        labels = {'title': 'title', 'description': 'description', 'author': 'author'}