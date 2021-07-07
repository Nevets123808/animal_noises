from unittest.mock import patch
from flask_testing import TestCase
from flask import url_for, jsonify
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimal(TestBase):
    def test_pig(self):
        with patch('random.choice') as c:
            c.return_value = "pig"
            response = self.client.get(url_for("get_animal"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"pig", response.data)
    
    def test_noise(self):
        package = {"data":"pig"}
        response = self.client.post(url_for("get_noise"), json = package)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"oink", response.data)