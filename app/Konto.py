class Konto:
    def __init__(self, imie, nazwisko,pesel, promo_code = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel = "Niepoprawny Pesel!"
        else:
            self.pesel = pesel
        if promo_code is not None:
            if promo_code.startswith('PROM_') and len(promo_code) == 8:
                self.saldo = 50
            else:
                self.saldo = 0