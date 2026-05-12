import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import sqlite3
from isletme import KiralamaSistemi
from tasitlar import Araba

class Uygulama:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Ultra Lüks Araç Kiralama - SQL Veritabanı")
        self.pencere.geometry("750x550")
        self.pencere.configure(bg="#f0f0f0")
        
        self.sistem = KiralamaSistemi()
        
        # BURASI HATA VEREN YERDİ, ARTIK DÜZELDİ
        self.verileri_yukle()

        tk.Label(pencere, text="💎 LÜKS ARAÇ YÖNETİM PANELİ (SQL)", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=15)

        # Tablo Tasarımı
        self.tablo = ttk.Treeview(pencere, columns=("Plaka", "Marka", "Model", "Yıl", "Saatlik"), show="headings")
        self.tablo.heading("Plaka", text="PLAKA"); self.tablo.heading("Marka", text="MARKA")
        self.tablo.heading("Model", text="MODEL"); self.tablo.heading("Yıl", text="YIL")
        self.tablo.heading("Saatlik", text="SAATLİK (TL)")
        self.tablo.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.tabloyu_guncelle()

        # Butonlar
        btn_frame = tk.Frame(pencere, bg="#f0f0f0")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="KİRALAMA YAP", command=self.kirala_penceresi, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), width=20, height=2).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="KİRALAMA GEÇMİŞİ", command=self.gecmis_goster, bg="#3498db", fg="white", font=("Arial", 10, "bold"), width=20, height=2).grid(row=0, column=1, padx=10)

    # İŞTE EKSİK OLAN VEYA HATALI YERLEŞTİRİLEN FONKSİYON BURASI:
    def verileri_yukle(self):
        try:
            baglanti = sqlite3.connect("araclar.db")
            cursor = baglanti.cursor()
            cursor.execute("SELECT * FROM araclar")
            veriler = cursor.fetchall()
            
            for v in veriler:
                # v[0]=plaka, v[1]=marka, v[2]=model, v[3]=yil, v[4]=ucret
                yeni_arac = Araba(v[0], v[1], v[2], v[3], v[4])
                self.sistem.arac_ekle(yeni_arac)
            
            baglanti.close()
        except Exception as e:
            messagebox.showerror("Veritabanı Hatası", f"Veriler SQL'den çekilemedi: {e}")

    def tabloyu_guncelle(self):
        for i in self.tablo.get_children(): self.tablo.delete(i)
        for a in self.sistem.araclar:
            ucret = a.ucret_hesapla(1) 
            self.tablo.insert("", "end", values=(a.plaka, a.marka, a.model, a.yil, ucret))

    def kirala_penceresi(self):
        secili = self.tablo.selection()
        if not secili:
            messagebox.showwarning("Uyarı", "Lütfen bir araç seçin!")
            return
        
        musteri = simpledialog.askstring("Müşteri Bilgisi", "Müşteri Adı Soyadı:")
        if not musteri: return
        
        saat = simpledialog.askinteger("Kiralama Süresi", "Kaç saat kiralayacaksınız?", minvalue=1)
        if not saat: return
            
        plaka = self.tablo.item(secili)["values"][0]
        ucret = self.sistem.arac_kirala(plaka, musteri, saat)
        messagebox.showinfo("İşlem Başarılı", f"Sayın {musteri},\nAraç: {plaka}\nToplam Tutar: {ucret} TL")

    def gecmis_goster(self):
        gecmis_pencere = tk.Toplevel(self.pencere)
        gecmis_pencere.title("Kiralama Kayıtları (Kalıcı Hafıza)")
        gecmis_pencere.geometry("550x350")
        liste = tk.Listbox(gecmis_pencere, font=("Arial", 10), width=80)
        liste.pack(pady=10, padx=10, fill="both", expand=True)
        
        if not self.sistem.gecmis:
            liste.insert(tk.END, "Henüz bir kayıt bulunmamaktadır.")
        else:
            for k in self.sistem.gecmis:
                satir = f"Müşteri: {k['musteri']} | Plaka: {k['plaka']} | Tutar: {k['tutar']} TL"
                liste.insert(tk.END, satir)

if __name__ == "__main__":
    root = tk.Tk()
    app = Uygulama(root)
    root.mainloop()