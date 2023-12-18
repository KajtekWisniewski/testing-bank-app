#refactor na dziedziczenie
import requests
from .Account import Account

class CompanyAccount(Account):
    def __init__(self, companyName, NIP):
        self.companyName = companyName
        self.balance = 0
        self.history = []
        self.express_transfer_fee = 5
        if len(NIP) != 10:
            self.NIP = "Invalid NIP!"
        else:
            self.NIP = NIP
    
    def express_transfer(self, amount):
        if amount > 0:
            self.outgoing_transfer(amount)
            self.balance -= self.express_transfer_fee
            self.history.append(-self.express_transfer_fee)

    def check_balance_for_credit(self, amount):
        if self.balance > amount*2:
            return True
        else:
            return False
    
    def check_zus_requirement(self, history):
        if -1775 in history:
            return True
        else:
            return False

    def get_credit(self, amount, history):
        if self.check_balance_for_credit(amount) and self.check_zus_requirement(history):
            self.balance+=amount
            return True
        else:
            return False
        
    def query_for_api(self, NIP):
        r = requests.get(f"https://wl-api.mf.gov.pl/api/search/nip/${NIP}?date=2023-12-17")
        if r.status_code == 200:
            print(r.status_code)
            return True
        else:
            print(r.status_code)
            return False