import unittest

from ..Account import Account
from ..CustomerAccount import CustomerAccount
from ..CompanyAccount import CompanyAccount
from unittest.mock import patch, MagicMock

class TestCreateBankAccount(unittest.TestCase):

    # customer account section #

    imie = 'Dariusz'
    nazwisko ='Januszewski'
    pesel = '89045678901'
    kodrabatowy = 'PROM_XYZ'

    def test_tworzenie_konta(self):
        first_acc = CustomerAccount(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(first_acc.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(first_acc.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(first_acc.balance, 0, "Saldo nie jest zerowe!")
        self.assertEqual(first_acc.pesel, self.pesel, "Pesel nie zostal odnaleziony")

    def test_pesel_with_len_10(self):
        konto = CustomerAccount(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.pesel, "Niepoprawny Pesel!", "Za krotki pesel zostal przyjety za prawidlowy")

    def test_pesel_with_len_12(self):
        konto = CustomerAccount(self.imie, self.nazwisko, "123456789001")
        self.assertEqual(konto.pesel, "Niepoprawny Pesel!", "Za krotki pesel zostal przyjety za prawidlowy")

    def test_empty_pesel(self):
        konto = CustomerAccount(self.imie, self.nazwisko, "")
        self.assertEqual(konto.pesel, "Niepoprawny Pesel!", "Za krotki pesel zostal przyjety za prawidlowy")

    def test_promo_wrong_preffix(self):
        konto = CustomerAccount(self.imie, self.nazwisko, self.pesel, "prom_123")
        self.assertEqual(konto.balance, 0, "Saldo nie jest zerowe")

    def test_promo_wrong_suffix(self):
        konto = CustomerAccount(self.imie, self.nazwisko, self.pesel,"PROM_1sdsd")
        self.assertEqual(konto.balance, 0, "Saldo nie jest zerowe")

    def test_promo_wrong_len(self):
        konto = CustomerAccount(self.imie, self.nazwisko, self.pesel,"PRO_123")
        self.assertEqual(konto.balance, 0, "Saldo nie jest zerowe")

    def test_promo_correct(self):
        konto = CustomerAccount(self.imie, self.nazwisko, self.pesel, self.kodrabatowy)
        self.assertEqual(konto.balance, 50, "promocja nienaliczona")

    def test_promo_year_59(self):
        konto = CustomerAccount(self.imie,self.nazwisko, '59045678901', self.kodrabatowy)
        self.assertEqual(konto.balance, 0, "promocja niepoprawnie naliczona")

    def test_promo_year_59_wrong_pesel_none(self):
        konto = CustomerAccount(self.imie,self.nazwisko, '59045678901152', self.kodrabatowy)
        is_none = konto.get_customer_age('Niepoprawny Pesel!')
        self.assertEqual(is_none, None, "nie jest none")

    def test_promo_is_customer_eligible(self):
        konto = CustomerAccount(self.imie,self.nazwisko, '59045678901152', self.kodrabatowy)
        is_none = konto.is_customer_eligible_for_promo('Niepoprawny Pesel!')
        self.assertFalse(is_none)

    def test_promo_year_60(self):
        konto = CustomerAccount(self.imie,self.nazwisko, '60045678901', self.kodrabatowy)
        self.assertEqual(konto.balance, 0, "promocja niepoprawnie naliczona")

    def test_promo_year_89(self):
        konto = CustomerAccount(self.imie,self.nazwisko, self.pesel, self.kodrabatowy)
        self.assertEqual(konto.balance, 50, "promocja nienaliczona")
    
    def test_promo_year_01(self):
        konto = CustomerAccount(self.imie,self.nazwisko, '01245678901', self.kodrabatowy)
        self.assertEqual(konto.balance, 50, "promocja nienaliczona")
    
    def test_promo_year_01_wrong_promo_code(self):
        konto = CustomerAccount(self.imie,self.nazwisko, '01245678901', "PRAZ_XYZZ")
        self.assertEqual(konto.balance, 0, "promocja niepoprwanie naliczona")

    def test_promo_year_59_correct_promo_code(self):
        konto = CustomerAccount(self.imie,self.nazwisko, '59045678901', self.kodrabatowy)
        self.assertEqual(konto.balance, 0, "promocja niepoprawnie naliczona")

    # company account section #

    companyName = "UG"
    NIP = "8461627563"

    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_creating_company_acc(self, mock_query_for_api):
        mock_query_for_api.return_value = True
        first_acc = CompanyAccount(self.companyName, self.NIP)
        self.assertEqual(first_acc.companyName, self.companyName, "Company name has not been saved!")
        self.assertEqual(first_acc.balance, 0, "Saldo nie jest zerowe!")
        self.assertEqual(first_acc.NIP, self.NIP, "NIP Has not been found")
    
    def test_NIP_with_len_9(self):
        first_acc = CompanyAccount(self.companyName, "890456789")
        self.assertEqual(first_acc.NIP, "Invalid NIP!", "NIP is too short")

    def test_NIP_with_len_11(self):
        first_acc = CompanyAccount(self.companyName, "890456789011")
        self.assertEqual(first_acc.NIP, "Invalid NIP!", "NIP is too long")
    
    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_NIP_that_deosnt_exist(self, mock_query_for_api):
        
        mock_query_for_api.return_value = False

        with self.assertRaises(ValueError) as context:
            first_acc = CompanyAccount(self.companyName, "8461627562")
        self.assertEqual(str(context.exception), "This NIP doesnt exist", "Unexpected error message")

    @patch('app.CompanyAccount.CompanyAccount.query_for_api')
    def test_query_for_api_false(self, mock_query_for_api):
        mock_query_for_api.return_value = False

        result = CompanyAccount.query_for_api("8461627562", "https://wl-test.mf.gov.pl/api/search/nip/8461627563?date=2023-12-01")
        self.assertEqual(result, False)

    # def test_query_for_api_false_no_mock(self):

    #     result = CompanyAccount.query_for_api(self, "8461627562", "https://wl-test.mf.gov.pl/api/search/nip/8461627563?date=2023-12-01")
    #     self.assertEqual(result, False)
    
    # def test_query_for_api_true_no_mock(self):

    #     result = CompanyAccount.query_for_api(self, "8461627563", "https://wl-api.mf.gov.pl")
    #     self.assertEqual(result, True)

    def test_account(self):
        first_acc = Account()
        self.assertEqual(first_acc.balance, 0, "Niezerowe saldo")
        self.assertEqual(first_acc.history, [], "Niepusta historia")