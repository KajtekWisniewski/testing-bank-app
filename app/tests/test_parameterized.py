import unittest

from ..Account import Account
from ..CustomerAccount import CustomerAccount
from ..CompanyAccount import CompanyAccount
from ..AccountRegistry import RegisterAccount

from parameterized import parameterized

class TestCredit(unittest.TestCase):

    companyName = "UG"
    NIP = "8904567890"

    # @parameterized.expand([
    # ([100, 100, 100], 500, True, 500),
    # ([100, 100, 100], -200, 500, False, 0),])

    # def test_loan_take_out(self, history, loan_amount, expected_output, expected_saldo):
    #     account = CustomerAccount(self.imie, self.nazwisko, self.pesel)
    #     account.history = historyis_loan = account.loan(loan_amount)
    #     self.assertEqual(account.balance, expected_output)

    @parameterized.expand([
    ([100, 100, -1775], 5000, 1200, True, 6200),
    ([100, 100, 100], 500, 900, False, 500),
    ([100, -1775, 100], 500, 900, False, 500),
    ([100, 100, 100], 5000, 900, False, 5000)
    ])

    
    def test_loan_take_out(self, history, balance, loan_amount, expected_output, expected_balance):
        account = CompanyAccount(self.companyName, self.NIP)
        account.balance = balance
        account.history = history
        is_loan = account.get_credit(loan_amount, history)
        self.assertEqual(account.balance, expected_balance)
        self.assertEqual(is_loan, expected_output)

    #setup
    @classmethod
    def setUpClass(cls):
        konto = CustomerAccount(cls.name, cls.nazwisko, cls.pesel)
        AccountRegistry.add_account(account)
