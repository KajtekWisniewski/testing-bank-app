import unittest

from ..Konto import Konto

class TestTransfer(unittest.TestCase):
    personal_data = {
        "name":"Dariusz",
        "surname": "Januszewski",
        "pesel": "89045678901"
    }

    def test_incoming_transfer(self):
        first_acc = Konto(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.incoming_transfer(100)
        self.assertEqual(first_acc.saldo, 100, "Srodki nie dotarly")

    # def test_incoming_transfer_0(self):
    #     first_acc = Konto(self.personal_data("name"), self.personal_data("surname"), self.personal_data("pesel"))
    #     first_acc.incoming_transfer(0)
    #     self.assertEqual(first_acc.saldo, "invalid_transfer", "Srodki nie dotarly")

    def test_incoming_transfer_incorrect_amount(self):
        first_acc = Konto(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.incoming_transfer(-100)
        self.assertEqual(first_acc.saldo, 0, "Saldo nie jest poprawne")

    def test_outcoming_transfer(self):
        first_acc = Konto(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.saldo = 150
        first_acc.outgoing_transfer(100)
        self.assertEqual(first_acc.saldo, 50, "Saldo nie jest poprawne")

    def test_outcoming_transfer_not_enough_cash(self):
        first_acc = Konto(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.saldo = 50
        first_acc.outgoing_transfer(100)
        self.assertEqual(first_acc.saldo, 50, "Saldo nie jest poprawne")
    
    