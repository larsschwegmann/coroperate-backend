from django.contrib.auth.models import User
from rest_framework.test import APITestCase, force_authenticate

from request.models import Profile

# Create your tests here.
class UserCreationTestCase(APITestCase):
    def setUp(self):
        self.userName = "Frank"
        self.password = 'secret_password'

    def test_1(self):
        response = self.client.post('/users/', {'username': 'Frank', 'password': 'secret_Frank'})
        print(response.data)

