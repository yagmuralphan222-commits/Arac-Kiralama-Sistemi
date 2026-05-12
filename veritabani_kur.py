import sqlite3

def tabloyu_olustur():
    # Veritabanına bağlan
    baglanti = sqlite3.connect("araclar.db")
    cursor = baglanti.cursor()

    # Önce eski tabloyu silelim ki yeni liste temizce yüklensin
    cursor.execute("DROP TABLE IF EXISTS araclar")

    # Tabloyu yeniden oluştur
    cursor.execute('''CREATE TABLE araclar (
                        plaka TEXT PRIMARY KEY,
                        marka TEXT,
                        model TEXT,
                        yil INTEGER,
                        ucret INTEGER)''')

    # GENİŞLETİLMİŞ ARAÇ LİSTESİ
    arac_listesi = [
        # Senin İstediğin Özel Araçlar
        ("00 FRT 0000", "Tesla", "Model S Plaid", 2024, 5000),
        ("04 YGMR 4848", "Lamborghini", "Urus Performante", 2024, 6000),
        ("06 BRT 0606", "Ferrari", "SF90 Stradale", 2024, 6000),
        ("11 FTH 1111", "Audi", "RS7 Sportback", 2024, 4500),
        ("04 APO 0404", "BMW", "M8 Competition", 2024, 4500),
        
        # Eklediğimiz Yeni Lüks ve Spor Araçlar
        ("34 POR 911", "Porsche", "911 Turbo S", 2025, 7000),
        ("34 RR 01", "Rolls-Royce", "Spectre", 2025, 9000),
        ("34 MER 63", "Mercedes-AMG", "G63", 2024, 5500),
        ("34 RAN 07", "Range Rover", "Autobiography", 2024, 4000),
        ("34 BUG 16", "Bugatti", "Chiron", 2023, 15000),
        ("34 AST 07", "Aston Martin", "DBS V12", 2024, 5000),
        
        # Popüler ve Prestijli Diğer Modeller
        ("34 VW 100", "Volkswagen", "Passat Business", 2024, 2000),
        ("34 SKO 01", "Skoda", "Superb L&K", 2024, 1800),
        ("34 FIA 50", "Fiat", "Egea Cross Limited", 2024, 1200),
        ("34 VOL 90", "Volvo", "XC90 Recharge", 2024, 3500)
    ]

    # Verileri SQL'e gönder
    cursor.executemany("INSERT INTO araclar VALUES (?,?,?,?,?)", arac_listesi)
    
    baglanti.commit()
    baglanti.close()
    print("Veritabanı güncellendi! Toplam " + str(len(arac_listesi)) + " araç yüklendi.")

tabloyu_olustur()