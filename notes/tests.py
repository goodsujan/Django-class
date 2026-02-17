from django.test import TestCase
from .utils import add


class AddTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 7)
