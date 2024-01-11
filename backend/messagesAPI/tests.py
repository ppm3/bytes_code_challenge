from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class MessageAPITests(APITestCase):
    def test_create_message(self):
        """
        Ensure we can create a new message.
        """
        url = reverse('message_list')
        data = {'message': 'Hello, world!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)