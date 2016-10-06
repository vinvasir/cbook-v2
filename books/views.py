from django.shortcuts import render

from .models import Author, ComicBook
# Create your views here.
def index(request):
    context = {'books': ComicBook.objects.all()}
    return render(request, 'books/index.html', context)