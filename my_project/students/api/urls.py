from django.urls import path, include
from rest_framework import routers
from .viewsets import StudentsModelViewSet


router = routers.DefaultRouter()
router.register('students', StudentsModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
