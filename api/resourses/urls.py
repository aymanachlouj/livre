from django.urls import path, include
from rest_framework import routers
from .book import BookViewSet
from .author import AuthorViewSet
from .cart import CartViewSet



router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'cart', CartViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
