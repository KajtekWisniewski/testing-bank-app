class Konto:
    def __init__(self, companyName, NIP):
        self.companyName = companyName
        self.balance = 0
        if len(NIP) != 10:
            self.NIP = "Incorrect NIP!"
        else:
            self.NIP = NIP
        
    def incoming_transfer(self, amount):
        if amount > 0:
            self.balance += amount
    
    def outgoing_transfer(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        