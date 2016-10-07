from django import forms
from .models import ComicBook, Author

class ComicBookForm(forms.Form):
    class Meta:
        model = ComicBook
        fields = ['title', 'description',]
        labels = {'title': 'title', 'description': 'description',}