from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^books/$', views.index, name='index'),
    url(r'^books/json/$', views.BookList.as_view(), name="book-index-json"),
    url(r'authors/json/$', views.AuthorList.as_view(), name='author-index-json'),
    url(r'authors/(?P<pk>\d+)/json/$', views.AuthorDetail.as_view(), name='author-detail-json'),
    url(r'^books/(?P<comic_book_id>\d+)/$', views.detail, name='detail'),
    url(r'^books/(?P<pk>\d+)/json/$', views.BookDetail.as_view(), name="book-detail-json"),
    url(r'^books/new/$', views.new, name='new'),
    url(r'^books/(?P<comic_book_id>\d+)/reviews', views.BookReviewList.as_view(), name='book-reviews'),
]