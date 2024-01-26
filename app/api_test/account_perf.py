import requests
import unittest

class testAccountCrud(unittest.TestCase):
    def setUp(cls):
        cls.url = "http://localhost:5000/api/accounts"
    
    post_data = {"imie": "Jacek", "nazwisko": "jaworek", "pesel": "89045678902"}


    def test_999XXX_CreateHundredAccounts(self):
        for i in range(0,10): #daje 10 zamiast 100 bo za dlugo trwa pipeline
                r = requests.post(self.url, json={"imie": "Jacek", "nazwisko": "Jaworek", "pesel": "89045678902"}, timeout=2)
                self.assertEqual(r.status_code, 201)
                r2 = requests.delete(self.url+"/89045678902", timeout=2)
                self.assertEqual(r2.status_code, 201)
                self.assertEqual(r2.json(), {"message": "successfuly deleted"})

#python -m unittest app/api_test/account_crud.py
#python -m flask --debug --app app/api.py run
#python -m coverage run -m unittest
#python -m coverage report
#docker compose -f mongo.yml up
    