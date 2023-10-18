import unittest

from ..Account import Account
from ..CustomerAccount import CustomerAccount
from ..CompanyAccount import CompanyAccount




class TestTransfer(unittest.TestCase):
    personal_data = {
        "name":"Dariusz",
        "surname": "Januszewski",
        "pesel": "89045678901"
    }
    company_data = {
        "companyName": "University",
        "NIP": "9845857821"
    }

    def test_incoming_transfer(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.incoming_transfer(100)
        self.assertEqual(first_acc.balance, 100, "Srodki nie dotarly")

    # def test_incoming_transfer_0(self):
    #     first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
    #     first_acc.incoming_transfer(0)
    #     self.assertEqual(first_acc.balance, 0, "Srodki niepoprawnie dotarly")

    def test_incoming_transfer_incorrect_amount(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.incoming_transfer(-100)
        self.assertEqual(first_acc.balance, 0, "Saldo nie jest poprawne")

    def test_outcoming_transfer(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.outgoing_transfer(100)
        self.assertEqual(first_acc.balance, 50, "Saldo nie jest poprawne")

    def test_outcoming_transfer_not_enough_cash(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 50
        first_acc.outgoing_transfer(100)
        self.assertEqual(first_acc.balance, 50, "Saldo nie jest poprawne")
    
    def test_company_incoming_transfer(self):
        first_company_acc = CompanyAccount(self.company_data["companyName"], self.company_data["NIP"])
        first_company_acc.incoming_transfer(100)
        self.assertEqual(first_company_acc.balance, 100, "Srodki nie dotarly")

    def test_company_outcoming_transfer(self):
        first_company_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_company_acc.balance = 150
        first_company_acc.outgoing_transfer(100)
        self.assertEqual(first_company_acc.balance, 50, "Saldo nie jest poprawne")