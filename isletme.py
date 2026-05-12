import json
import os
from tasitlar import Araba

class KiralamaSistemi:
    def __init__(self):
        self.araclar = []
        self.gecmis = []
        self.dosya_adi = "gecmis.json"
        self.gecmisi_yukle() # Program açılırken eski kayıtları getir

    def arac_ekle(self, arac):
        self.araclar.append(arac)

    def arac_kirala(self, plaka, musteri_adi, saat):
        for arac in self.araclar:
            if arac.plaka == plaka:
                toplam = arac.ucret_hesapla(saat)
                kayit = {
                    "musteri": musteri_adi,
                    "arac": arac.marka,
                    "plaka": plaka,
                    "sure": saat,
                    "tutar": toplam
                }
                self.gecmis.append(kayit)
                self.gecmisi_kaydet() # Her kiralamada dosyayı güncelle
                return toplam
        return None

    def gecmisi_kaydet(self):
        # Verileri kalıcı olarak JSON dosyasına yazar
        with open(self.dosya_adi, "w", encoding="utf-8") as f:
            json.dump(self.gecmis, f, ensure_ascii=False, indent=4)

    def gecmisi_yukle(self):
        # Program açıldığında dosyadan verileri okur
        if os.path.exists(self.dosya_adi):
            with open(self.dosya_adi, "r", encoding="utf-8") as f:
                self.gecmis = json.load(f)