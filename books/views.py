from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from rest_framework import generics

from .models import Author, Genre, ComicBook, Review
from .serializers import AuthorSerializer, GenreSerializer, ComicBookSerializer, ReviewSerializer
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

class BookList(generics.ListCreateAPIView):
    queryset = ComicBook.objects.all()
    serializer_class = ComicBookSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComicBook.objects.all()
    serializer_class = ComicBookSerializer

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookReviewList(generics.ListCreateAPIView):
    model = Review
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = super(BookReviewList, self).get_queryset()
        return queryset.filter(comic_book__pk = self.kwargs.get('comic_book_id'))