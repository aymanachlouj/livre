from rest_framework import viewsets
from .serializers import AuthorSerializer
from book_shelf.models import Author
from rest_framework import permissions


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.AllowAny, )
