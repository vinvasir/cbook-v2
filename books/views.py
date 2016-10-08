from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import AuthorSerializer

from .models import Author, ComicBook
from .forms import ComicBookForm
# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

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

def author_list(request):
    """
    List all authors, or create a new author.
    """
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)    