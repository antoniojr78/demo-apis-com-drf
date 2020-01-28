from django.test import TestCase, Client
from rest_framework import status

'''https://docs.djangoproject.com/en/2.1/topics/testing/overview/
python my_project/manage.py test students
python my_project/manage.py test students.tests
python my_project/manage.py test students.tests.StudentsTests
python my_project/manage.py test students.tests.StudentsTests.test_get_students
'''


class StudentsTests(TestCase):
    def test_get_students(self):
        client = Client()
        response = client.get('/api/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
