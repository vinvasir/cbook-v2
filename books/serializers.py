from .models import Author, ComicBook, Review
from rest_framework import serializers

# A custom SlugRelatedField for creating a new object if one doesn't exist.
# Found at http://stackoverflow.com/questions/28009829/creating-and-saving-foreign-key-objects-using-a-slugrelatedfield
class CreatableSlugRelatedField(serializers.SlugRelatedField):

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('pk', 'name', 'created_at')

class ComicBookSerializer(serializers.ModelSerializer):
    author = CreatableSlugRelatedField(slug_field='name', queryset=Author.objects.all())

    class Meta:
        model = ComicBook
        fields = ('pk', 'title', 'description', 'author')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('pk', 'content', 'rating', 'comic_book', 'user', 'created_at')