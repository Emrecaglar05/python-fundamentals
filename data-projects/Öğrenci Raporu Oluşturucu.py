import csv

with open("ogrenci_notlari.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)  # csv dosyasını satır satır okur (reader)
    for row in reader:
        print(row)

with open("ogrenci_notlari.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # csv dosyasını sözlük gibi okur (DictReader)
    for row in reader:
        print(row)

with open("ogrenci_notlari2.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)  # Yeni bir csv dosyasına Aynı kolonlarla eleman ekler.
    writer.writerow(['Isim', 'Matematik', 'Fen', 'Ingilizce'])
    writer.writerow(["Emre", 95, 54, 56])

import csv

##### Öğrenci Raporu Oluşturucu #####

def ogrenci_raporu_olustur(giris_dosyasi, cikis_dosyasi):
    try:
        # Adım 1: Öğrenci verilerini oku
        with open(giris_dosyasi, 'r', encoding="utf-8") as infile:
            okuyucu = csv.DictReader(infile)
            raporlar = []

            for satir in okuyucu:
                isim = satir['Isim']
                matematik = int(satir['Matematik'])
                fen = int(satir['Fen'])
                ingilizce = int(satir['Ingilizce'])

                # Ortalama hesapla
                ortalama = round((matematik + fen + ingilizce) / 3, 2)

                # Geçti / Kaldı durumu
                durum = "Geçti" if ortalama >= 60 else "Kaldı"

                raporlar.append({
                    'Isim': isim,
                    'Matematik': matematik,
                    'Fen': fen,
                    'Ingilizce': ingilizce,
                    'Ortalama': ortalama,
                    'Durum': durum
                })

        # Adım 2: Yeni CSV dosyasına yaz
        with open(cikis_dosyasi, 'w', newline='', encoding="utf-8") as outfile:
            alanlar = ['Isim', 'Matematik', 'Fen', 'Ingilizce', 'Ortalama', 'Durum']
            yazici = csv.DictWriter(outfile, fieldnames=alanlar)
            yazici.writeheader()
            yazici.writerows(raporlar)

            print(f"✅ Öğrenci raporu '{cikis_dosyasi}' dosyasına başarıyla kaydedildi.")

    except FileNotFoundError:
        print(f"❌ Hata: '{giris_dosyasi}' dosyası bulunamadı.")
    except KeyError:
        print("❌ Hata: Giriş dosyasındaki kolon adları yanlış (Isim, Matematik, Fen, Ingilizce olmalı).")
    except Exception as e:
        print(f"❌ Beklenmeyen bir hata oluştu: {e}")


# Ana Program
giris_dosyasi = 'ogrenci_notlari.csv'      # Giriş dosyası (öğrenci notları)
cikis_dosyasi = 'ogrenci_raporu.csv'       # Çıkış dosyası (rapor)
ogrenci_raporu_olustur(giris_dosyasi, cikis_dosyasi)
