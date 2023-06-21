from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class PokemonCreationTestCase(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='admin')
        self.user = User.objects.create_user(username='user', password='user')

    def test_pokemon_creation(self):
        self.client.force_authenticate(user=self.admin)
        data = {'dexNumber': '4', 'name': 'Charmander', 'ability': 'Mar Llamas'}
        res = self.client.post(f'/pokemon/create', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_pokemon_creation_no_authorized(self):
        self.client.force_authenticate(user=self.user)
        data = {'dexNumber': '4', 'name': 'Charmander', 'ability': 'Mar Llamas'}
        res = self.client.post(f'/pokemon/create', data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)