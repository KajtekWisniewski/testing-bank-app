import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    imietestowe = 'Dariusz'
    nazwiskotestowe ='Januszewski'

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imietestowe, self.nazwiskotestowe)
        self.assertEqual(pierwsze_konto.imie, self.imietestowe, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwiskotestowe, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    #tutaj proszę dodawać nowe testy