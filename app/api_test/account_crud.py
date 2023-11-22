#testy api aby dzialac potrzebuj aby aplikacja dzialala
import requests
import unittest

class testAccountCrud(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/api/accounts"
    
