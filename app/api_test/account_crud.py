#testy api aby dzialac potrzebuj aby aplikacja dzialala
import requests
import unittest

class testAccountCrud(unittest.TestCase):
    def setUp(cls):
        cls.url = "http://localhost:5000/api/accounts"
    
    post_data = {"imie": "Jacek", "nazwisko": "jaworek", "pesel": "89045678902"}
    #to ma byc json zeby dzialalo

    def test_1_PostCreatAcc(self):
        r = requests.post(self.url, json={"imie": "Jacek", "nazwisko": "Jaworek", "pesel": "89045678902"})
        self.assertEqual(r.status_code, 201)
    
    def test_2_GetAccountByPesel(self):
        r = requests.get(self.url+"/89045678902")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"balance": 0, "name": "Jacek", "nazwisko": "Jaworek", "pesel": "89045678902" })
    
    def test_3_GetAccountByWrongPesel(self):
        r = requests.get(self.url+"/8904567890212")
        self.assertEqual(r.status_code, 404)    

    def test_4_GetAccountsCount(self):
        r = requests.get(self.url+"/count")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"message": "There are 1 accounts in the database"})
    
    def test_5_purge(self):
        r = requests.delete(self.url+"/PURGE")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"message": "sucessfuly emptied the list"})

    @classmethod
    def tearDownClass(cls):
        requests.delete(cls.url+"/PURGE")
    