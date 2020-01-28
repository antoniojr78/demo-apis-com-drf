from rest_framework import viewsets
from .serializers import StudentSerializer
from ..models import Student


class StudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()  # .filter(active=True)
    serializer_class = StudentSerializer
