#from .Account import Account
from pymongo import MongoClient
from .CustomerAccount import CustomerAccount

class RegisterAccount():

    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    collection = db['konta']
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
    def find_account_with_pesel(cls, pesel):
        accountToFind = next((account for account in cls.listOfAccounts if account.pesel == pesel), None)
        if accountToFind is not None:
            return accountToFind
        else:
            return None
        
    @classmethod
    def save(cls):
        cls.collection.delete_many({})

        for account in cls.listOfAccounts:
            account_data = {
                'imie': account.imie,
                'nazwisko': account.nazwisko,
                'pesel': account.pesel,
                'balance': account.balance,
                'history': account.history
            }
            cls.collection.insert_one(account_data)
    
    @classmethod
    def load(cls):
        cls.listOfAccounts = []
        for account_data in cls.collection.find():
            account = CustomerAccount(account_data['imie'], account_data['nazwisko'], account_data['pesel'])
            account.balance = account_data['balance']
            account.history = account_data['history']
            cls.listOfAccounts.append(account)