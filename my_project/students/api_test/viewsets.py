from rest_framework import views, status, response
from ..api.serializers import StudentSerializer
from ..models import Student


'''This type de API needs token authentication
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),'''
class StudentsAPIView(views.APIView):
    def get(self, request):
        serializer = StudentSerializer()
        return Response({'cases': serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
