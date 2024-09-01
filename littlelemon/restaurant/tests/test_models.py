from django.test import TestCase
from restaurant.models import Menu
import sys
import os

print(sys.path)


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")