from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from rest_framework import generics

from .models import Author, ComicBook
from .serializers import AuthorSerializer
from .forms import ComicBookForm
# Create your views here.

def home(request):
    return render(request, 'books/home.html')

def index(request):
    context = {'books': ComicBook.objects.all()}
    return render(request, 'books/index.html', context)

def detail(request, comic_book_id):
    book = ComicBook.objects.get(id=comic_book_id)
    context = {'book': book}
    return render(request, 'books/detail.html', context)

@login_required
def new(request):
    if request.method != 'POST':
        form = ComicBookForm()
    else:
        form = ComicBookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:index'))

    context = {'form': form}
    return render(request, 'books/new.html', context)

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer