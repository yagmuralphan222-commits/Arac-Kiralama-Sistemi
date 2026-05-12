class Tasit:
    def __init__(self, plaka, marka, model, yil):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.yil = yil

class Araba(Tasit):
    def __init__(self, plaka, marka, model, yil, gunluk_ucret):
        super().__init__(plaka, marka, model, yil)
        # Kapsülleme (Encapsulation): Ücreti gizli tutuyoruz
        self.__gunluk_ucret = gunluk_ucret 

    def ucret_hesapla(self, gun):
        return self.__gunluk_ucret * gun

    def __str__(self):
        return f"{self.marka} {self.model} ({self.yil}) - Plaka: {self.plaka}"