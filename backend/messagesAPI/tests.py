import uuid
from .models import Message
from django.urls import reverse
from django.test import TestCase
from rest_framework import status

class HealthCheckTestCase(TestCase):
    def test_health_check(self):
        """	
        Test suite for the health check endpoint.
        """
        url = reverse('health_check')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('uptime', response.data)
        
class PingTestCase(TestCase):
    def test_ping(self):
        """
        Test suite for the ping endpoint.
        """
        url = reverse('ping')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'PONG')
        

class MessageListTestCase(TestCase):
    def setUp(self):
        self.valid_payload = {
            'to': 'recipient@example.com',
            'subject': 'Test Subject',
            'body': 'Test Body'
        }
        self.invalid_payload = {
            'subject': 'Missing To and Body'
        }
        
    def test_create_message_with_valid_payload(self):
        """
        Ensure we can create a new message with valid payload.
        """
        url = reverse('message_list')
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['to'], self.valid_payload['to'])
        self.assertEqual(response.data['subject'], self.valid_payload['subject'])
        self.assertEqual(response.data['body'], self.valid_payload['body'])
        self.assertTrue('id' in response.data)
    
    def test_create_message_with_invalid_payload(self):
        """
        Ensure we cannot create a new message with invalid payload.
        """
        url = reverse('message_list')
        response = self.client.post(url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class MessageDetailAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.message1 = Message.objects.create(to='user1@example.com', subject='Test Subject 1', body='Test Body 1')
        cls.message2 = Message.objects.create(to='user2@example.com', subject='Test Subject 2', body='Test Body 2')

    def test_get_valid_message(self):
        """	
        Ensure we can get a message by id.
        """
        url = reverse('message_detail', args=[self.message1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['to'], self.message1.to)
        self.assertEqual(response.data['subject'], self.message1.subject)
        self.assertEqual(response.data['body'], self.message1.body)

    def test_get_invalid_message(self):
        """
        Ensure we get a 404 response when trying to get a message that does not exist.
        """
        url = reverse('message_detail', args=[str(uuid.uuid4())])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_message(self):
        """
        Ensure we can update a message.
        """
        url = reverse('message_detail', args=[self.message1.id])
        data = {'to': 'updated@example.com', 'subject': 'Updated Subject', 'body': 'Updated Body'}
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['to'], data['to'])
        self.assertEqual(response.data['subject'], data['subject'])
        self.assertEqual(response.data['body'], data['body'])
    
    def test_update_message_not_found(self):
        """
        Ensure we get a 404 response when trying to update a message that does not exist.
        """
        url = reverse('message_detail', args=[str(uuid.uuid4())])
        response = self.client.put(url, {})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_message_invalid_payload(self):
        """
        Ensure we get a 400 response when trying to update a message with invalid payload.
        """
        url = reverse('message_detail', args=[self.message1.id])
        response = self.client.put(url, {}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_message(self):
        """
        Ensure we can delete a message.
        """
        url = reverse('message_detail', args=[self.message2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Message.objects.filter(id=self.message2.id).exists())
