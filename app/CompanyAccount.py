#refactor na dziedziczenie

from .Account import Account

class CompanyAccount(Account):
    def __init__(self, companyName, NIP):
        self.companyName = companyName
        self.balance = 0
        if len(NIP) != 10:
            self.NIP = "Invalid NIP!"
        else:
            self.NIP = NIP
    
    def express_transfer(self, amount):
        if amount > 0:
            self.outgoing_transfer(amount+5)
    


        