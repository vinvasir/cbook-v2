from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.views import Response
from .serializers import AuthorSerializer

from .models import Author, ComicBook
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

class AuthorList(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)