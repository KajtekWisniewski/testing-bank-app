class Konto:
    def __init__(self, imie, nazwisko,pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel = "Niepoprawny Pesel!"
        else:
            self.pesel = pesel