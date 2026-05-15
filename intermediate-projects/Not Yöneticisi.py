# ---------------------------
# Liste Anlamaları (List Comprehensions)
# ---------------------------

# Kareleri al
kareler = [x**2 for x in range(10)]
print("Kareler:", kareler)

# Sayıları iki ile çarp
sayilar = [1, 2, 3, 4, 5]
iki_kat = [x * 2 for x in sayilar]
print("İki katı:", iki_kat)

# Çift sayıları filtrele
sayilar = [1, 2, 3, 4, 5, 6, 7]
ciftler = [x for x in sayilar if x % 2 == 0]
print("Çift sayılar:", ciftler)

# Kısa isimleri filtrele (5 harften kısa)
isimler = ["Alice", "Bob", "Charlie", "Dave"]
kisa_isimler = [isim for isim in isimler if len(isim) < 5]
print("Kısa isimler:", kisa_isimler)

# Even/Odd etiketleme
sayilar = [1, 2, 3, 4, 5, 6]
etiketler = ["Çift" if x % 2 == 0 else "Tek" for x in sayilar]
print("Etiketler:", etiketler)


# ---------------------------
# Öğrenci Not Yönetimi
# ---------------------------

# 1. Adım: Öğrenci notlarını al
ogrenci_notlari = input("Öğrenci notlarını virgülle ayırarak girin: ")
notlar = [int(not_) for not_ in ogrenci_notlari.split(",")]

# 2. Adım: Notları harflerle eşleştir
harf_notlari = [
    "A" if not_ >= 90 else
    "B" if not_ >= 80 else
    "C" if not_ >= 70 else
    "D" if not_ >= 60 else
    "F"
    for not_ in notlar
]

# 3. Adım: Başarılı ve başarısız öğrencileri filtrele
basarili_ogrenciler = [not_ for not_ in notlar if not_ >= 60]
basarisiz_ogrenciler = [not_ for not_ in notlar if not_ < 60]

# 4. Adım: Sonuçları yazdır
print("\n--- Öğrenci Notları ---")
for i, (not_, harf) in enumerate(zip(notlar, harf_notlari), start=1):
    print(f"Öğrenci {i}: Not = {not_}, Harf Notu = {harf}")

print("\n--- Başarılı ve Başarısız Öğrenciler ---")
print("Başarılı Öğrenciler:", basarili_ogrenciler)
print("Başarısız Öğrenciler:", basarisiz_ogrenciler)
