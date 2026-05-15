# -*- coding: utf-8 -*-

DOSYA_ADI = "tarifler.txt"

# Tarifleri okuma ve listeleme fonksiyonu
def tarif_goruntule():
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as file:
            tarifler = file.read().strip().split("\n\n")  #  split :Tarif bloklarını ayırır.| strip : boş blokları temizler.
            tarifler = [tarif.strip() for tarif in tarifler if tarif.strip()]

        if not tarifler:
            print("Henüz tarif yok!")
            return

        # Tarif adlarını çıkart
        tarif_adlari = []
        for tarif in tarifler:
            satirlar = tarif.split("\n")
            for satir in satirlar:
                if satir.startswith("Tarif:"):
                    tarif_adlari.append(satir.replace("Tarif:", "").strip())
                    break

        print("\n--- Tarifler ---")
        for isim in tarif_adlari:
            print(f"- {isim}")

        secim = input("\nGörüntülemek istediğiniz tarifin adını yazın: ").strip()
        if secim in tarif_adlari:
            # İlgili tarifi bul ve göster
            index = tarif_adlari.index(secim)
            print(f"\nSeçtiğiniz Tarif:\n{tarifler[index]}")
        else:
            print("Tarif bulunamadı.")

    except FileNotFoundError:
        print("Tarif dosyası bulunamadı. Lütfen tarif ekleyin.")

# Yeni tarif ekleme fonksiyonu
def tarif_ekle():
    print("\n--- Yeni Tarif Ekle ---")
    isim = input("Tarif adı: ").strip()
    malzemeler = input("Malzemeler (virgülle ayırın): ").strip()
    yapim = input("Yapımı: ").strip()

    with open(DOSYA_ADI, "a", encoding="utf-8") as file:
        file.write(f"Tarif: {isim}\n")
        file.write(f"Malzemeler: {malzemeler}\n")
        file.write(f"Yapımı: {yapim}\n\n")

    print(f"'{isim}' tarifi başarıyla eklendi!")

# Ana program döngüsü
while True:
    print("\n--- Tarif Defteri ---")
    print("1. Tarifleri Görüntüle")
    print("2. Yeni Tarif Ekle")
    print("3. Çıkış")
    secim = input("Seçiminizi girin (1/2/3): ").strip()

    if secim == "1":
        tarif_goruntule()
    elif secim == "2":
        tarif_ekle()
    elif secim == "3":
        print("Programdan çıkılıyor. Hoşçakal!")
        break
    else:
        print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")
