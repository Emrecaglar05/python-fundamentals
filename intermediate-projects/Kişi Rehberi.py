rehber = {}

def menu_goster():
    print("\n--- Rehber Menüsü ---")
    print("1. Kişi Ekle")
    print("2. Kişileri Görüntüle")
    print("3. Kişi Ara")
    print("4. Kişi Düzenle")
    print("5. Kişi Sil")
    print("6. Çıkış")

def kisi_ekle():
    isim = input("Kişi adı: ")
    telefon = input("Telefon numarası: ")
    email = input("E-posta: ")
    rehber[isim] = {"telefon": telefon, "email": email}
    print(f"{isim} rehbere eklendi.")

def kisileri_goruntule():
    if rehber:
        for isim, bilgiler in rehber.items():
            print(f"\nAd: {isim}")
            print(f"Telefon: {bilgiler['telefon']}")
            print(f"E-posta: {bilgiler['email']}")
    else:
        print("Rehber boş.")

def kisi_ara():
    isim = input("Aramak istediğiniz kişinin adı: ")
    if isim in rehber:
        print(f"Telefon: {rehber[isim]['telefon']}")
        print(f"E-posta: {rehber[isim]['email']}")
    else:
        print("Bu kişi rehberde yok.")

def kisi_duzenle():
    isim = input("Düzenlemek istediğiniz kişinin adı: ")
    if isim in rehber:
        telefon = input("Yeni telefon: ")
        email = input("Yeni e-posta: ")
        rehber[isim] = {"telefon": telefon, "email": email}
        print(f"{isim} güncellendi.")
    else:
        print("Bu kişi bulunamadı.")

def kisi_sil():
    isim = input("Silmek istediğiniz kişinin adı: ")
    if isim in rehber:
        del rehber[isim]
        print(f"{isim} silindi.")
    else:
        print("Bu kişi bulunamadı.")

# Ana döngü
while True:
    menu_goster()
    secim = input("Seçiminiz: ")

    if secim == "1":
        kisi_ekle()
    elif secim == "2":
        kisileri_goruntule()
    elif secim == "3":
        kisi_ara()
    elif secim == "4":
        kisi_duzenle()
    elif secim == "5":
        kisi_sil()
    elif secim == "6":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.")
