from django.urls import path
from .viewsets import StudentsAPIView


urlpatterns = [
    path("students_test_token/", StudentsAPIView.as_view()),
]
