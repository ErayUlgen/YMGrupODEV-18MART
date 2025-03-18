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


def personel_modulu():
    print("\n--- Personel Modülü ---")
    print("1) Personel Ekle")
    print("2) Personel İzin Güncelle")
    print("3) Personel Maaş Görüntüle")
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        isim = input("Yeni personel ismi: ")
        pozisyon = input("Pozisyonu: ")
        print(f"{isim} adlı personel {pozisyon} olarak eklendi (örnek).")
    elif secim == "2":
        pid = input("İzin güncellenecek personel ID: ")
        yeni_izin = input("Yeni izin gün sayısı: ")
        print(f"Personel {pid} için izin gün sayısı {yeni_izin} olarak güncellendi (örnek).")
    elif secim == "3":
        pid = input("Maaşı görüntülenecek personel ID: ")
        print(f"Personel {pid} maaşı: 8000 TL (örnek).")
    else:
        print("Geçersiz seçim!")

def stok_tasima():
    print("\n--- Şubeler Arası Stok Taşıma ---")
    kaynak = input("Kaynak şube: ")
    hedef = input("Hedef şube: ")
    urun = input("Taşınacak ürün: ")
    miktar = input("Miktar: ")
    print(f"{kaynak} şubesinden {hedef} şubesine {miktar} adet/kilo {urun} taşındı (örnek).")
