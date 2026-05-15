####### KISA ALIŞTIRMA ########

with open("günlük.txt", "w", encoding="utf-8") as file:                  # w modu dosya yazma işlemidir.
    file.write("Gün 1:, Bugün Python'da dosya yazmayı öğrendim. \n")

with open("günlük.txt", "a", encoding="utf-8") as file:
    file.write("Gün 2:, Bugün ilk Günlüğümü oluşturdum. \n")            # a modu mevcut dosyaya ekleme yapma işlemidir.


####### GÜNLÜK KAYDEDİCİ ########

dosya_adi = 'günlük.txt'

def ekleme():   # Yeni Günlük Ekleme
    yazi = input("Günlüğünüzü yazınız: ")
    with open(dosya_adi, "a", encoding="utf-8") as file:
        file.write(yazi + '\n')
        print("Başarıyla Eklendi")

def girileri_goruntuleme():
    try:
        with open(dosya_adi, "r", encoding="utf-8") as file:
            icerik = file.read()
            if icerik:
                print("\n--- Günlüğünüz---")
                print(icerik)
            else:
                print("Bir Günlük Yok")
    except FileNotFoundError:
        print("Dosya Bulunamadı")

def girdi_ara(): # Günlük Arama
    anahtar_kelime = input("Aramak için kelime girin: ").lower()
    try:
        with open(dosya_adi, "r", encoding="utf-8") as file:
            icerik = file.readlines()
            bulunan = False
            print(f"\n--- '{anahtar_kelime}' İçeren Günlük Kayıtları ---")
            for satir in icerik:
                if anahtar_kelime in satir.lower():
                    print(satir.strip())
                    bulunan = True
            if not bulunan:
                print("Aradığınız kelimeye ait kayıt bulunamadı.")
    except FileNotFoundError:
        print("Dosya Bulunamadı")

# Ana Menü
while True:
    print("\n--- Günlük Uygulaması ---")
    print("1. Günlük Ekle")
    print("2. Günlükleri Görüntüle")
    print("3. Günlükte Ara")
    print("4. Çıkış")

    secim = input("Seçiminizi yapın (1-4): ")

    if secim == "1":
        ekleme()
    elif secim == "2":
        girileri_goruntuleme()
    elif secim == "3":
        girdi_ara()
    elif secim == "4":
        print("Çıkış yapılıyor. Hoşçakal!")
        break
    else:
        print("Geçersiz seçim. Lütfen 1-4 arasında bir sayı girin.")




