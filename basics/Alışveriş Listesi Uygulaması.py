# -------------------------------
# Alışveriş Listesi Uygulaması
# -------------------------------

# Adım 1: Boş bir alışveriş listesi başlat
alisveris_listesi = []

# Adım 2: Menü fonksiyonu tanımla
def menu_goster():
    print("\n--- Alışveriş Listesi Menüsü ---")
    print("1. Listeyi Görüntüle")
    print("2. Ürün Ekle")
    print("3. Ürün Sil")
    print("4. Listeyi Temizle")
    print("5. Çıkış")

# Adım 3: Ana Program Döngüsü
while True:
    menu_goster()
    secim = input("Seçiminizi yapın (1-5): ")

    if secim == "1":
        print("\n--- Alışveriş Listesi ---")
        if not alisveris_listesi:
            print("Alışveriş listeniz boş.")
        else:
            for index, urun in enumerate(alisveris_listesi):
                print(f"{index + 1}. {urun}")

    elif secim == "2":
        urun = input("Eklemek istediğiniz ürünü girin: ")
        alisveris_listesi.append(urun)
        print(f"{urun}, alışveriş listesine eklendi.")

    elif secim == "3":
        urun = input("Silmek istediğiniz ürünü girin: ")
        if urun in alisveris_listesi:
            alisveris_listesi.remove(urun)
            print(f"{urun}, alışveriş listesinden silindi.")
        else:
            print(f"{urun}, alışveriş listesinde yok.")

    elif secim == "4":
        alisveris_listesi.clear()
        print("Alışveriş listesi temizlendi.")

    elif secim == "5":
        print("Hoşçakal! İyi alışverişler 🛒")
        break

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
