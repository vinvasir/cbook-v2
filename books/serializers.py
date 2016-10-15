from .models import Author, ComicBook, Review
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('pk', 'name', 'created_at')

class ComicBookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = ComicBook
        fields = ('pk', 'title', 'description', 'author')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('pk', 'content', 'rating', 'comic_book', 'user', 'created_at')