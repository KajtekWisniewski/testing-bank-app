import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    imie = 'Dariusz'
    nazwisko ='Januszewski'
    pesel = '89345678901'
    kodrabatowy = 'PROM_XYZ'

    def test_tworzenie_konta(self):
        first_acc = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(first_acc.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(first_acc.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(first_acc.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(first_acc.pesel, self.pesel, "Pesel nie zostal odnaleziony")

    def test_pesel_with_len_10(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.pesel, "Niepoprawny Pesel!", "Za krotki pesel zostal przyjety za prawidlowy")

    def test_pesel_with_len_12(self):
        konto = Konto(self.imie, self.nazwisko, "123456789001")
        self.assertEqual(konto.pesel, "Niepoprawny Pesel!", "Za krotki pesel zostal przyjety za prawidlowy")

    def test_empty_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "")
        self.assertEqual(konto.pesel, "Niepoprawny Pesel!", "Za krotki pesel zostal przyjety za prawidlowy")

    def test_promo_wrong_preffix(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "prom_123")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")

    def test_promo_wrong_suffix(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel,"PROM_1sdsd")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")

    def test_promo_wrong_len(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel,"PRO_123")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")

    def test_promo_correct(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel,"PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "promo nie naliczone")

    def test_promo_year_59(self):
        konto = Konto(self.imie,self.nazwisko, 59345678901)

    def test_promo_year_60(self):
        konto = Konto(self.imie,self.nazwisko, 89345678901)

    def test_promo_year_89(self):
        konto = Konto(self.imie,self.nazwisko, self.pesel)
    
    def test_promo_year_01(self):
        konto = Konto(self.imie,self.nazwisko, '00145678901')
    
    def test_promo_year_01_wrong_promo_code(self):
        konto = Konto(self.imie,self.nazwisko, '00145678901', "PRAZ_XYZZ")

    def test_promo_year_59_correct_promo_code(self):
        konto = Konto(self.imie,self.nazwisko, 59345678901, "PROM_XYZ")
    #tutaj proszę dodawać nowe testy