import unittest

from ..Account import Account
from ..CustomerAccount import CustomerAccount
from ..CompanyAccount import CompanyAccount
from ..AccountRegistry import RegisterAccount

from parameterized import parameterized

class TestCredit(unittest.TestCase):

    companyName = "UG"
    NIP = "8904567890"

    name = "Jack"
    nazwisko = "Menel"
    pesel = "89045678901"

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
    #f14 tests
    @classmethod
    def setUpClass(cls):
        account = CustomerAccount(cls.name, cls.nazwisko, cls.pesel)
        RegisterAccount.add_account(account)
    
    def test_adding_first_acc(self):
        acc = CustomerAccount(self.name, self.nazwisko, self.pesel)
        acc1 = CustomerAccount(self.name + "ddd", self.nazwisko, "89045678902")
        RegisterAccount.add_account(acc)
        RegisterAccount.add_account(acc1)
        self.assertEqual(RegisterAccount.how_many_accs(), 3)
        self.assertEqual(RegisterAccount.find_account_with_pesel(self.pesel).pesel, acc.pesel)
        self.assertEqual(RegisterAccount.find_account_with_pesel("89045678903"), None)

    @classmethod
    def tearDownClass(cls):
        RegisterAccount.listOfAccounts = []
