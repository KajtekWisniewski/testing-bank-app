import unittest

from ..Account import Account
from ..CustomerAccount import CustomerAccount
from ..CompanyAccount import CompanyAccount
from parameterized import parameterized
from unittest.mock import patch, MagicMock


class TestTransfer(unittest.TestCase):
    personal_data = {
        "name":"Dariusz",
        "surname": "Januszewski",
        "pesel": "89045678901"
    }
    company_data = {
        "companyName": "University",
        "NIP": "8461627563"
    }

    def setUp(self):
        self.account = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])

    #example for setUp
    #self.account.history = history
    #is_credit_accepted = self.account.get_credit(amount)

    #@parameterized.expand([
    # ([100, 100, 100], 500, True, 500)
    # ])

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
    
    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_company_incoming_transfer(self, mock_query_for_api):
        mock_query_for_api.return_value = True
        first_company_acc = CompanyAccount(self.company_data["companyName"], self.company_data["NIP"])
        first_company_acc.incoming_transfer(100)
        self.assertEqual(first_company_acc.balance, 100, "Srodki nie dotarly")

    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_company_express_transfer(self, mock_query_for_api):
        mock_query_for_api.return_value = True
        first_company_acc = CompanyAccount(self.company_data["companyName"], self.company_data["NIP"])
        first_company_acc.balance = 150
        first_company_acc.express_transfer(100)
        self.assertEqual(first_company_acc.balance, 45, "Saldo nie jest poprawne")

    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_company_express_transfer_5(self, mock_query_for_api):
        mock_query_for_api.return_value = True
        first_company_acc = CompanyAccount(self.company_data["companyName"], self.company_data["NIP"])
        first_company_acc.balance = 150
        first_company_acc.express_transfer(150)
        self.assertEqual(first_company_acc.balance, -5, "Saldo nie jest poprawne")

    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_company_express_history(self, mock_query_for_api):
        mock_query_for_api.return_value = True
        first_company_acc = CompanyAccount(self.company_data["companyName"], self.company_data["NIP"])
        first_company_acc.balance = 150
        first_company_acc.express_transfer(150)
        self.assertEqual(first_company_acc.history, [-150,-5], "Saldo nie jest poprawne")

    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_company_incoming_history(self, mock_query_for_api):
        mock_query_for_api.return_value = True
        first_company_acc = CompanyAccount(self.company_data["companyName"], self.company_data["NIP"])
        first_company_acc.balance = 150
        first_company_acc.incoming_transfer(150)
        self.assertEqual(first_company_acc.history, [150], "Saldo nie jest poprawne") 

    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_company_outgoing_history(self, mock_query_for_api):
        mock_query_for_api.return_value = True
        first_company_acc = CompanyAccount(self.company_data["companyName"], self.company_data["NIP"])
        first_company_acc.balance = 150
        first_company_acc.outgoing_transfer(150)
        self.assertEqual(first_company_acc.history, [-150], "Saldo nie jest poprawne")    

    def test_customer_express_transfer(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.express_transfer(100)
        self.assertEqual(first_acc.balance, 49, "Saldo nie jest poprawne")
    
    def test_customer_express_transfer_1(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 3
        first_acc.express_transfer(3)
        self.assertEqual(first_acc.balance, -1, "Saldo nie jest poprawne")

    def test_customer_outgoing_transfer_history(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.outgoing_transfer(100)
        self.assertEqual(first_acc.history, [-100], "Historia jest pusta")
    
    def test_customer_incoming_transfer_history(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.incoming_transfer(100)
        self.assertEqual(first_acc.history, [100], "Historia jest pusta")
    
    def test_customer_express_transfer_history(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.express_transfer(100)
        self.assertEqual(first_acc.history, [-100, -1], "Historia jest pusta")

    def test_customer_get_credit_1st_condition(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.history = [-100, 200, 100, 100]
        is_given = first_acc.customer_get_credit(500)
        self.assertEqual(first_acc.balance, 650, "Nie dodano kredytu")
        self.assertEqual(first_acc.history, [-100, 200, 100, 100, 500], "Nie dodano do historii")
        self.assertTrue(is_given)

    def test_customer_get_credit_2nd_condition(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.history = [-100, 200, 100, 600, -200]
        is_given = first_acc.customer_get_credit(500)
        self.assertEqual(first_acc.balance, 650, "Nie dodano kredytu")
        self.assertEqual(first_acc.history, [-100, 200, 100, 600, -200, 500], "Nie dodano do historii")
        self.assertTrue(is_given)
    
    def test_customer_get_credit_not_enough_transactions(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.history = [-100, 200]
        is_given = first_acc.customer_get_credit(500)
        self.assertEqual(first_acc.balance, 150, "Blednie dodano kredyt")
        self.assertEqual(first_acc.history, [-100, 200], "Blednie dodano do historii")
        self.assertFalse(is_given)
    
    def test_customer_get_credit_wrong_first_condition(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.history = [-100, 200, 500]
        is_given = first_acc.customer_get_credit(500)
        self.assertEqual(first_acc.balance, 150, "Blednie dodano kredyt")
        self.assertEqual(first_acc.history, [-100, 200, 500], "Blednie dodano do historii")
        self.assertFalse(is_given)

    def test_customer_get_credit_wrong_second_condition(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.history = [-900, -300, 200, 100, -500]
        is_given = first_acc.customer_get_credit(500)
        self.assertEqual(first_acc.balance, 150, "Blednie dodano kredyt")
        self.assertEqual(first_acc.history, [-900, -300, 200, 100, -500], "Blednie dodano do historii")
        self.assertFalse(is_given)
    
    def test_customer_get_credit_wrong_second_condition_but_first_correct(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.history = [-900, -300, 200, 100, 500]
        is_given = first_acc.customer_get_credit(500)
        self.assertEqual(first_acc.balance, 650, "Nie dodano kredyt")
        self.assertEqual(first_acc.history, [-900, -300, 200, 100, 500, 500], "Nie dodano do historii")
        self.assertTrue(is_given)
    
    def test_customer_get_credit_empty_history(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.history = []
        is_given = first_acc.customer_get_credit(500)
        self.assertEqual(first_acc.balance, 150, "Blednie dodano kredyt")
        self.assertEqual(first_acc.history, [], " Blednie dodano do historii")
        self.assertFalse(is_given)
    
    def test_customer_get_credit_long_list_(self):
        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.balance = 150
        first_acc.history = [-100,-300,500,-300,-200,100,100,100]
        is_given = first_acc.customer_get_credit(500)
        self.assertEqual(first_acc.balance, 650, "Blednie NIE dodano kredyt")
        self.assertEqual(first_acc.history, [-100,-300,500,-300,-200,100,100,100, 500], " Blednie NIE dodano do historii")
        self.assertTrue(is_given)
    

