from rest_framework import serializers
from book_shelf.models import Book

class BookSerializer(serializers.ModelSerializer):
    authorName = serializers.CharField(source='author.name', read_only=True)
    class Meta:
        model = Book
        fields = ['title', 'authorName', 'description','cover',]
