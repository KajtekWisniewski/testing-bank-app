import unittest

from ..Account import Account
from ..CustomerAccount import CustomerAccount
from ..CompanyAccount import CompanyAccount
from ..SMTPConnection import SMTPConnection
from unittest.mock import patch, MagicMock
from datetime import date

class TestSMTPConnection(unittest.TestCase):

    personal_data = {
        "name":"Dariusz",
        "surname": "Januszewski",
        "pesel": "89045678901"
    }

    company_data = {
        "companyName": "University",
        "NIP": "8461627563"
    }

    def test_sending_customer_mail_history_true(self):
        smtp_connection_mock = MagicMock(spec=SMTPConnection)      
        smtp_connection_mock.wyslij.return_value = True

        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.history = [-100, 200, 100]

        today = date.today()
        poprawny_temat = f"Wyciag z dnia {today}"
        poprawna_tresc = f"Historia konta to: {first_acc.history}"
        result = first_acc.send_customer_mail_history("test@example.com", smtp_connection_mock)
        smtp_connection_mock.wyslij.assert_called_once_with(poprawny_temat, poprawna_tresc, "test@example.com")
        self.assertTrue(result)
    
    def test_sending_customer_mail_history_false(self):
        smtp_connection_mock = MagicMock(spec=SMTPConnection)     
        smtp_connection_mock.wyslij.return_value = False

        first_acc = CustomerAccount(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        first_acc.history = [-100, 200, 100]

        today = date.today()
        poprawny_temat = f"Wyciag z dnia {today}"
        poprawna_tresc = f"Historia konta to: {first_acc.history}"

        result = first_acc.send_customer_mail_history("test@example.com", smtp_connection_mock)
        smtp_connection_mock.wyslij.assert_called_once_with(poprawny_temat, poprawna_tresc, "test@example.com")
        self.assertFalse(result)
    
    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_sending_company_mail_history_true(self, mock_query_for_api):
        smtp_connection_mock = MagicMock(spec=SMTPConnection)     
        smtp_connection_mock.wyslij.return_value = True
        mock_query_for_api.return_value = True

        first_acc = CompanyAccount(self.company_data["companyName"], self.company_data["NIP"])
        first_acc.history = [-100, 200, 100]

        today = date.today()
        poprawny_temat = f"Wyciag z dnia {today}"
        poprawna_tresc = f"Historia konta Twojej firmy to: {first_acc.history}"

        result = first_acc.send_company_mail_history("test@example.com", smtp_connection_mock)
        smtp_connection_mock.wyslij.assert_called_once_with(poprawny_temat, poprawna_tresc, "test@example.com")
        self.assertTrue(result)
    
    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_sending_company_mail_history_false(self, mock_query_for_api):
        smtp_connection_mock = MagicMock(spec=SMTPConnection)     
        smtp_connection_mock.wyslij.return_value = False
        mock_query_for_api.return_value = True

        first_acc = CompanyAccount(self.company_data["companyName"], self.company_data["NIP"])
        first_acc.history = [-100, 200, 100]

        today = date.today()
        poprawny_temat = f"Wyciag z dnia {today}"
        poprawna_tresc = f"Historia konta Twojej firmy to: {first_acc.history}"

        result = first_acc.send_company_mail_history("test@example.com", smtp_connection_mock)
        smtp_connection_mock.wyslij.assert_called_once_with(poprawny_temat, poprawna_tresc, "test@example.com")
        self.assertFalse(result)

