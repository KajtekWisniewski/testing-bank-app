#testy api aby dzialac potrzebuj aby aplikacja dzialala
import requests
import unittest

class testAccountCrud(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/api/accounts"
    
    post_data = {"imie": "Jacek", "nazwisko": "jaworek", "pesel": "89045678902"}
    #to ma byc json zeby dzialalo

    def testPostCreatAcc(self):
        r = requests.post(self.url, data = self.post_data)
        self.assertEqual(r.status_code, 201)