# isletme.py
from tasitlar import Araba # Modüler yapı: Başka dosyadan sınıf çağırma 

class KiralamaSistemi:
    def __init__(self):
        self.mevcut_araclar = []

    def arac_ekle(self, arac):
        self.mevcut_araclar.append(arac)

    def listele(self):
        print("\n--- Galerideki Araçlar ---")
        for i, arac in enumerate(self.mevcut_araclar):
            print(f"{i+1}. {arac.bilgi_goster()} - Günlük: {arac.get_ucret()} TL")