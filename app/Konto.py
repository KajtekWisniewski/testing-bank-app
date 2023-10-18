class Konto:
    def __init__(self, imie, nazwisko,pesel, promo_code = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel = "Niepoprawny Pesel!"
        else:
            self.pesel = pesel
        if self.is_promo_code_correct(promo_code) and self.is_customer_eligible_for_promo(pesel):
            self.saldo = 50
        else:
            self.saldo = 0
    
    def is_promo_code_correct(self, promo_code):
        if promo_code is None:
            return False
        if promo_code.startswith('PROM_') and len(promo_code) == 8:
            return True
        else:
            return False
    
    def get_customer_age(self, pesel):
        if (pesel == "Niepoprawny Pesel!"):
            return None
        customerDecade = int(pesel[2])
        customerYearOfBirth = int(str(pesel[0:2]))
        currentYear = 23
        if customerDecade == 0:
            return 100 - customerYearOfBirth + currentYear
        return currentYear-customerYearOfBirth
    
    def is_customer_eligible_for_promo(self, pesel):
        customer_age = self.get_customer_age(pesel)
        if customer_age == None:
            return False
        if customer_age > 60:
            return False
        return True
    
    def incoming_transfer(self, amount):
        if amount > 0:
            self.saldo += amount
    
    def outgoing_transfer(self, amount):
        if amount > 0 and amount <= self.saldo:
            self.saldo -= amount
    
        

    