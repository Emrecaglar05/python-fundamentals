# ---------------------------
# Not Alma Uygulaması
# ---------------------------

# 1. Adım: Dosya adı tanımla
DOSYA_ADI = "notlarim.txt"

# 2. Adım: Menü gösterme fonksiyonu
def menu_goster():
    print("\n--- Not Alma Uygulaması Menüsü ---")
    print("1. Yeni not ekle")
    print("2. Tüm notları görüntüle")
    print("3. Tüm notları sil")
    print("4. Çıkış")

# 3. Adım: Yeni not ekleme
def not_ekle():
    not_ = input("Notunuzu girin: ")
    with open(DOSYA_ADI, "a") as dosya:
        dosya.write(not_ + "\n")
    print("Not başarıyla eklendi!")

# 4. Adım: Tüm notları görüntüleme
def notlari_goruntule():
    try:
        with open(DOSYA_ADI, "r") as dosya:
            icerik = dosya.read()
            if icerik:
                print("\n--- Tüm Notlar ---")
                print(icerik)
            else:
                print("\nHiç not bulunamadı.")
    except FileNotFoundError:
        print("Hiç not bulunamadı.")

# 5. Adım: Tüm notları silme
def notlari_sil():
    onay = input("Tüm notları silmek istediğinize emin misiniz? (Evet/hayır): ")
    if onay.lower() == "evet":
        with open(DOSYA_ADI, "w") as dosya:
            pass
        print("Tüm notlar silindi.")
    else:
        print("Silme işlemi iptal edildi.")

# 6. Adım: Ana program döngüsü
while True:
    menu_goster()
    secim = input("Seçiminizi girin (1-4): ")

    if secim == "1":
        not_ekle()
    elif secim == "2":
        notlari_goruntule()
    elif secim == "3":
        notlari_sil()
    elif secim == "4":
        print("Not Alma Uygulamasından çıkılıyor. Hoşça kalın!")
        break
    else:
        print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir sayı girin.")
