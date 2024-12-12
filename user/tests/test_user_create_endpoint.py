from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class UserCreateEndpointTest(TestCase):
    def setUp(self):
        # Initialize the API client
        self.client = APIClient()
        self.url = reverse('user-create')
        self.valid_payload = {
            'username': 'testuser',
            'password': 'Test@1234',
            'email': 'testuser@yopmail.com',
        }
        self.invalid_payload = {
            'username': '',  # Invalid as username is required
            'password': '123',  # Too short
            'email': 'not-an-email',
        }

    def test_user_creation_with_valid_data(self):
        # Send a POST request with valid data
        response = self.client.post(self.url, data=self.valid_payload, format='json')

        # Assert the response status and data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)

        # Assert the user was created in the database
        user = User.objects.get(username=self.valid_payload['username'])
        self.assertIsNotNone(user)
        self.assertEqual(user.email, self.valid_payload['email'])

    def test_user_creation_with_invalid_data(self):
        # Send a POST request with invalid data
        response = self.client.post(self.url, data=self.invalid_payload, format='json')

        # Assert the response status and data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertIn('password', response.data)
        self.assertIn('email', response.data)

    def test_user_creation_with_missing_fields(self):
        # Test creating a user with missing fields
        response = self.client.post(self.url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertIn('password', response.data)
