from unittest.mock import patch
from flask_testing import TestCase
from flask import url_for, jsonify
from requests_mock import Mocker

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestServer(TestBase):
    def test_animal(self):
        with Mocker() as mocker:
            mocker.get("http://api:5000/getanimal", json = {"data":"pig"})
            mocker.post("http://api:5000/getnoise", json = {"data":"oink"})        
            response = self.client.get(url_for("home"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"The pig goes oink", response.data)