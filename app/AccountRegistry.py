from .Account import Account

class RegisterAccount():

    listOfAccounts = []

    #cls -> class, operuje na calej klasie
    #self -> na instancji klasy

    @classmethod
    def add_account(cls, account):
        cls.listOfAccounts.append(account)
    
    @classmethod
    def how_many_accs(cls):
        return len(cls.listOfAccounts)
    
    @classmethod
    def find_account_with_pesel(cls):
        cls.listOfAccount
        return None