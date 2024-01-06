import unittest

from ..CompanyAccount import CompanyAccount
from ..AccountRegistry import RegisterAccount
from unittest.mock import patch, MagicMock

class TestMongo(unittest.TestCase):

    @patch('app.AccountRegistry.RegisterAccount.collection')
    def test_load_accs_from_database(self, mock_collection):
        
        mock_collection.find.return_value = [
            {"imie": "Jacek",
            "nazwisko": "Jaworek",
            "pesel":"89092909875",
             "balance": 0,
              "history": [] }
        ]
        RegisterAccount.load()
        self.assertEqual(len(RegisterAccount.listOfAccounts), 1)
        self.assertEqual(RegisterAccount.listOfAccounts[0].imie, 'Jacek')
    
    @patch('app.AccountRegistry.RegisterAccount.collection')
    def test_save_accs_to_database(self, mock_collection):

        mock_account = MagicMock()
        mock_account.pesel = "89092909875"
        mock_account.balance = 0
        mock_account.history = []
        mock_account.imie = "Jack"
        mock_account.nazwisko = "Jawor"

        RegisterAccount.listOfAccounts.append(mock_account)
        RegisterAccount.save()

        expected_data = {
            'imie': "Jack",
            'nazwisko': "Jawor",
            'pesel': "89092909875",
            'balance': 0,
            'history': []
        }
        mock_collection.insert_one.assert_called_with(expected_data)