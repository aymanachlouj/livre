from django.urls import include, path
from api.resourses import ressources_urls


urlpatterns = [
    path('api/', include(ressources_urls)),
]

