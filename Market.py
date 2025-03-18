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
    
    def salamanra_ayarla():
    print("\n--- Salamanra Ayarları ---")
    istenen_sicaklik = input("İstenen sıcaklık (°C): ")
    istenen_nem = input("İstenen nem (%): ")
    dondur = input("Dondurulacak mı? (E/H): ")
    print(f"Salamanra ayarlandı -> Sıcaklık: {istenen_sicaklik}°C, Nem: {istenen_nem}%, Dondur: {dondur}")

def stok_raporu():
    print("\n--- Stok / Satış Raporu ---")
    print("Bu örnekte veri yapısı kullanılmadığı için gerçek stok bilgisi tutulmuyor.")
    print("Sadece rapor fonksiyonunun örnek çalışması.")
