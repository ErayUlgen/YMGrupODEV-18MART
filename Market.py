def akilli_kasa():
    print("\n--- Akıllı Kasa ---")
    urun = input("Ürün adı: ")
    miktar = float(input("Miktar (kg/adet): "))
    fiyat = float(input("Birim fiyat: "))
    toplam = miktar * fiyat
    print(f"{urun} için toplam tutar: {toplam} TL")
    odeme = input("Ödeme yöntemi (Nakit / POS / RFID): ")
    print(f"Ödeme yöntemi: {odeme}")

def patane_reyonu():
    print("\n--- Patane Reyonu ---")
    print("Burada patates, soğan vb. ürünlerin satışı yapılır.")
    print("Basit reyon işlemleri gösterilir.")
    
def saklama_ayarla():
    print("\n--- Salamanra Ayarları ---")
    istenen_sicaklik = input("İstenen sıcaklık (°C): ")
    istenen_nem = input("İstenen nem (%): ")
    dondur = input("Dondurulacak mı? (E/H): ")
    print(f"Salamanra ayarlandı -> Sıcaklık: {istenen_sicaklik}°C, Nem: {istenen_nem}%, Dondur: {dondur}")

def stok_raporu():
    print("\n--- Stok / Satış Raporu ---")
    print("Bu örnekte veri yapısı kullanılmadığı için gerçek stok bilgisi tutulmuyor.")
    print("Sadece rapor fonksiyonunun örnek çalışması.")

def tedarik():
    print("\n--- Tedarik (Stok Arttırma) ---")
    sube = input("Tedarik yapılacak şube adı: ")
    urun = input("Ürün adı: ")
    miktar = input("Eklenecek miktar: ")
    print(f"{sube} şubesine {miktar} adet/kilo {urun} eklendi (örnek).")

def siparis():
    print("\n--- Sipariş (Stok Azaltma) ---")
    sube = input("Sipariş yapılan şube adı: ")
    urun = input("Satılacak ürün adı: ")
    miktar = input("Satılacak miktar: ")
    print(f"{sube} şubesinde {urun} stokundan {miktar} düşüldü (örnek).")
def kar_zarar_analizi():
    print("\n--- Kar/Zarar Analizi ---")
    urun = input("Analizi yapılacak ürün adı: ")
    maliyet = float(input("Ürünün maliyeti: "))
    satis_fiyati = float(input("Ürünün satış fiyatı: "))
    adet = float(input("Satılan adet/ miktar: "))
    kar = (satis_fiyati - maliyet) * adet
    print(f"{urun} için toplam kâr: {kar} TL")

def main():
    while True:
        print("\n=== BASİT MARKET YÖNETİM SİSTEMİ ===")
        print("1) Akıllı Kasa")
        print("2) Patane Reyonu")
        print("3) Salamanra Ayarları")
        print("4) Stok / Satış Raporu")
        print("5) Tedarik (Stok Arttırma)")
        print("6) Sipariş (Stok Azaltma)")
        print("7) Personel Modülü")
        print("8) Şubeler Arası Stok Taşıma")
        print("9) Kar/Zarar Analizi")
        print("0) Çıkış")
        
        secim = input("Seçiminiz: ")
        if secim == "1":
            akilli_kasa()
        elif secim == "2":
            patane_reyonu()
        elif secim == "3":
            salamanra_ayarla()
        elif secim == "4":
            stok_raporu()
        elif secim == "5":
            tedarik()
        elif secim == "6":
            siparis()
        elif secim == "7":
            personel_modulu()
        elif secim == "8":
            stok_tasima()
        elif secim == "9":
            kar_zarar_analizi()
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.")

if _name_ == "_main_":
    main()