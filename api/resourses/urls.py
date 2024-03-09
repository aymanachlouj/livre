from django.urls import path, include
from rest_framework import routers
from .book import BookViewSet
from .author import AuthorViewSet
from .cart import CartViewSet
from .user import UserRegistrationAPIView



router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'cart', CartViewSet)
"""router.register(r'registrer', UserRegistrationAPIView)"""

"""
router.register(r'login', UserListCreateAPIView)
"""


urlpatterns = [
    path('', include(router.urls)),
]
