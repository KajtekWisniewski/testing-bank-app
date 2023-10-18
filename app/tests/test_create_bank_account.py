import unittest

from ..Account import Account
from ..CustomerAccount import CustomerAccount
from ..CompanyAccount import CompanyAccount

class TestCreateBankAccount(unittest.TestCase):

    imie = 'Dariusz'
    nazwisko ='Januszewski'
    pesel = '89045678901'
    kodrabatowy = 'PROM_XYZ'

    companyName = "UG"
    NIP = "8904567890"

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

    def test_creating_company_acc(self):
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
    #tutaj proszę dodawać nowe testy