from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer  # Adjust the import according to your project structure


class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few test instances of the Menu model
        Menu.objects.create(title="Fish", price=80, inventory=100)
        Menu.objects.create(title="Potatoes", price=80, inventory=100)
        Menu.objects.create(title="Raw Stuff", price=80, inventory=100)

        self.client = APIClient()

    def test_getall(self):
        # Make a GET request to the endpoint that retrieves all Menu objects
        response = self.client.get('/restaurant/menu/')  # Adjust the URL to match your endpoint

        # Retrieve all Menu objects from the database
        menus = Menu.objects.all()

        # Serialize the data
        serializer = MenuItemSerializer(menus, many=True)

        # Check if the response data is equal to the serialized data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
