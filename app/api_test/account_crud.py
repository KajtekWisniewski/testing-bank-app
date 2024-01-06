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
        self.assertEqual(r.json(), {"balance": 0, "imie": "Jacek", "nazwisko": "Jaworek", "pesel": "89045678902" })
    
    def test_3_GetAccountByWrongPesel(self):
        r = requests.get(self.url+"/8904567890212")
        self.assertEqual(r.status_code, 404)    

    def test_4_GetAccountsCount(self):
        r = requests.get(self.url+"/count")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"message": "There are 1 accounts in the database"})
    
    def test_5_PatchMethod(self):
        r = requests.patch(self.url+"/89045678902", json={"imie": "Jacek", "nazwisko": "Jaworek", "pesel": "89045678902", "balance": 50})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"balance": 50, "imie": "Jacek", "nazwisko": "Jaworek", "pesel": "89045678902" })
    
    def test_8x_DeleteMethod(self):
        r = requests.delete(self.url+"/89045678902")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"message": "successfuly deleted"})
        r2 = requests.get(self.url+"/count")
        self.assertEqual(r2.status_code, 201)
        self.assertEqual(r2.json(), {"message": "There are 0 accounts in the database"})

    def test_7a_unique_pesel(self):
        r = requests.post(self.url, json={"imie": "Jacek", "nazwisko": "Jaworek", "pesel": "89045678902"})
        self.assertEqual(r.status_code, 409)
        self.assertEqual(r.json(), {"message": "Account with given pesel already exists"})
    
    def test_7b_GetAccountsCountIsCorrectAfterWrongPeselAttempt(self):
        r = requests.get(self.url+"/count")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"message": "There are 1 accounts in the database"})
    
    def test_8a_Successful_incoming_transfer(self):
        r = requests.post(self.url+"/89045678902/transfer", json={"amount": 550, "type": "incoming"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {"message": "incoming transfer accepted for fulfillment"})

    def test_8b_check_for_correct_balance(self):
        r = requests.get(self.url+"/89045678902")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"balance": 600, "imie": "Jacek", "nazwisko": "Jaworek", "pesel": "89045678902" })
    
    def test_8c_Successful_outgoing_transfer(self):
        r = requests.post(self.url+"/89045678902/transfer", json={"amount": 300, "type": "outgoing"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {"message": "outgoing transfer accepted for fulfillment"})

    def test_8d_check_for_correct_balance(self):
        r = requests.get(self.url+"/89045678902")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"balance": 300, "imie": "Jacek", "nazwisko": "Jaworek", "pesel": "89045678902" })
    
    def test_8e_failed_outgoing_transfer_not_enough_cash(self):
        r = requests.post(self.url+"/89045678902/transfer", json={"amount": 3000, "type": "outgoing"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {"message": "outgoing transfer accepted for fulfillment"})
    
    def test_8f_check_for_correct_balance_after_failed_outgoing(self):
        r = requests.get(self.url+"/89045678902")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"balance": 300, "imie": "Jacek", "nazwisko": "Jaworek", "pesel": "89045678902" })

    def test_9a_failed_incoming_transfer_acc_not_found(self):
        r = requests.post(self.url+"/89045678902/transfer", json={"amount": 550, "type": "incoming"})
        self.assertEqual(r.status_code, 404)
        self.assertEqual(r.json(), {"message": "account not found"})

    def test_9b_purge(self):
        r = requests.delete(self.url+"/PURGE")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json(), {"message": "sucessfuly emptied the list"})
    
    def test_8g_save_method(self):
        r = requests.patch(self.url+"/save")
        self.assertEqual(r.json(), {"message": "successfuly saved"})

    def test_8h_load_method(self):
        r = requests.patch(self.url+"/load")
        self.assertEqual(r.json(), {"message": "successfuly loaded"})

#python -m unittest app/api_test/account_crud.py
#python -m flask --debug --app app/api.py run
#python -m coverage run -m unittest
#python -m coverage report
    