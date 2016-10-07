from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Author, ComicBook
from .forms import ComicBookForm
# Create your views here.
def index(request):
    context = {'books': ComicBook.objects.all()}
    return render(request, 'books/index.html', context)

def detail(request, comic_book_id):
    book = ComimcBook.objects.get(id=comic_book_id)
    context = {'book': book}
    return render(request, 'books/detail.html', context)

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