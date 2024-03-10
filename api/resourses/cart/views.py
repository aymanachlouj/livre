from rest_framework import viewsets
from .serializers import CartSerializer
from book_shelf.models import Cart
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response




class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (permissions.AllowAny, )

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        cart = self.get_object()
        books = cart.books.all()  # Récupérer tous les livres associés au panier
        serialized_books = self.get_serializer(books, many=True).data
        return Response(serialized_books)