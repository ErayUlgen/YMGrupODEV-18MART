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