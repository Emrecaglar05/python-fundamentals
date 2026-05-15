import json
import os

# Görevlerin saklanacağı dosya
GOREV_DOSYASI = 'gorevler.json'

# Eğer dosya yoksa boş listeyle oluştur
if not os.path.exists(GOREV_DOSYASI):
    with open(GOREV_DOSYASI, 'w', encoding='utf-8') as file:
        json.dump([], file, ensure_ascii=False)

# Görevleri yükle
def yukle_gorevler():
    with open(GOREV_DOSYASI, 'r', encoding='utf-8') as file:
        return json.load(file)

# Görevleri kaydet
def kaydet_gorevler(gorevler):
    with open(GOREV_DOSYASI, 'w', encoding='utf-8') as file:
        json.dump(gorevler, file, indent=2, ensure_ascii=False)

# Yeni görev ekle
def gorev_ekle():
    gorev_adi = input("Görev adını girin: ").strip()
    gorevler = yukle_gorevler()
    gorevler.append({"gorev": gorev_adi, "durum": "Tamamlanmadı"})
    kaydet_gorevler(gorevler)
    print(f'"{gorev_adi}" görevi eklendi!')

# Görevleri görüntüle
def gorevleri_goster():
    gorevler = yukle_gorevler()
    if gorevler:
        print("\n--- Görev Listesi ---")
        for i, g in enumerate(gorevler, start=1):
            print(f"{i}. {g['gorev']} - {g['durum']}")
    else:
        print("Henüz görev bulunmuyor.")

# Görev durumunu güncelle
def durum_guncelle():
    gorevler = yukle_gorevler()
    gorevleri_goster()
    try:
        secim = int(input("Durumu güncellenecek görevin numarasını girin: ")) - 1
        if 0 <= secim < len(gorevler):
            yeni_durum = input("Yeni durumu girin (Tamamlandı/Tamamlanmadı): ").strip()
            gorevler[secim]['durum'] = yeni_durum
            kaydet_gorevler(gorevler)
            print("Görev durumu güncellendi!")
        else:
            print("Geçersiz görev numarası.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

# Görev sil
def gorev_sil():
    gorevler = yukle_gorevler()
    gorevleri_goster()
    try:
        secim = int(input("Silinecek görevin numarasını girin: ")) - 1
        if 0 <= secim < len(gorevler):
            silinen = gorevler.pop(secim)
            kaydet_gorevler(gorevler)
            print(f'"{silinen["gorev"]}" görevi silindi!')
        else:
            print("Geçersiz görev numarası.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

# Menü
def menu_goster():
    print("\n--- Mini Yapılacaklar Uygulaması ---")
    print("1. Yeni görev ekle")
    print("2. Görevleri görüntüle")
    print("3. Görev durumunu güncelle")
    print("4. Görev sil")
    print("5. Çıkış")

# Ana döngü
while True:
    menu_goster()
    secim = input("Seçiminizi girin (1-5): ").strip()

    if secim == '1':
        gorev_ekle()
    elif secim == '2':
        gorevleri_goster()
    elif secim == '3':
        durum_guncelle()
    elif secim == '4':
        gorev_sil()
    elif secim == '5':
        print("Uygulamadan çıkılıyor. Hoşça kal!")
        break
    else:
        print("Geçersiz seçim. 1 ile 5 arasında bir sayı giriniz.")
