from django.urls import path, include
from rest_framework import routers
from .viewsets import AuthorViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]