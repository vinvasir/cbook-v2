from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^books/$', views.index, name='index'),
    url(r'^books/(?P<comic_book_id>\d+)/$', views.detail, name='detail'),
    url(r'^books/new/$', views.new, name='new'),
]