from unittest.mock import patch
from flask_testing import TestCase
from flask import url_for
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimal(TestBase):
    def test_pig(self):
        with patch('choice') as c:
            c.return_value = "pig"
            response = client.get(url_for("/getanimal"))
            self.assertIn(b"pig", response.data)