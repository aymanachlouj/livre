from rest_framework import viewsets
from .serializers import BookSerializer
from book_shelf.models import Book
from rest_framework import permissions


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.AllowAny, )
