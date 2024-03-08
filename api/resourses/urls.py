from django.urls import path, include
from rest_framework import routers
from .book import BookViewSet
from .author import AuthorViewSet



router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
