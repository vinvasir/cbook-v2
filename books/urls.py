from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<comic_book_id>\d+)/$', views.detail, name='detail'),
    url(r'^new/$', views.new, name='new'),
]