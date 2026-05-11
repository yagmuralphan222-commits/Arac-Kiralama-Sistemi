# tasitlar.py

class Tasit:
    """Temel Sınıf (Base Class) - Kalıtım için kullanılacak"""
    def __init__(self, marka, model, gunluk_ucret):
        self.marka = marka
        self.model = model
        # Kapsülleme (Encapsulation): __ işareti ile bu veriyi dışarıya kapattık [cite: 20]
        self.__gunluk_ucret = gunluk_ucret 

    def bilgi_goster(self):
        return f"{self.marka} {self.model}"

    def get_ucret(self): # Kapsüllenmiş veriye güvenli erişim metodu
        return self.__gunluk_ucret

class Araba(Tasit):
    """Kalıtım (Inheritance) Uygulaması [cite: 20]"""
    def __init__(self, marka, model, gunluk_ucret, vites_tipi):
        # Üst sınıfın özelliklerini devralıyoruz
        super().__init__(marka, model, gunluk_ucret)
        self.vites_tipi = vites_tipi

    def bilgi_goster(self): # Polimorfizm: Aynı isimli metodu Araba için özelleştirdik
        return f"Araba: {self.marka} {self.model} - Vites: {self.vites_tipi}"