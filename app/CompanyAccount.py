#refactor na dziedziczenie

from .Account import Account

class CompanyAccount(Account):
    def __init__(self, companyName, NIP):
        self.companyName = companyName
        self.balance = 0
        if len(NIP) != 10:
            self.NIP = "Niepoprawny NIP!"
        else:
            self.NIP = NIP



        