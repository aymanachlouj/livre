from rest_framework import viewsets
from .serializers import CartSerializer
from book_shelf.models import Cart
from rest_framework import permissions


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (permissions.AllowAny, )
