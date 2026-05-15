sayi = 4

if sayi > 5:
  print("Sayı 5'ten büyük.")
elif sayi == 5:
  print("Sayı 5'e eşit.")
elif sayi == 4:
  print("Sayı 4'e eşit.")
else:
  print("Sayı 5'ten küçük.")

a = 2
b = 20

if a > 5 or b < 15:
  print("Koşullardan en az biri doğru.")
else:
  print("Her iki koşul da yanlış.")

# Sayı Karşılaştırma Aracı

# Adım 1: Kullanıcıdan iki sayı al
sayi1 = float(input("Birinci sayıyı gir: "))
sayi2 = float(input("İkinci sayıyı gir: "))

# Adım 2: Sayıları karşılaştır
print("\n--- Karşılaştırma Sonuçları ----")

if sayi1 == sayi2:
    print(f"Her iki sayı da eşit: {sayi1}")
elif sayi1 > sayi2:
    print(f"{sayi1}, {sayi2}'den büyüktür.")
else:
    print(f"{sayi2}, {sayi1}'den büyüktür.")

# Adım 3: Sıfır kontrolü yap
if sayi1 == 0 or sayi2 == 0:
    print("\nEn az bir sayı sıfırdır.")
else:
    print("\nHer iki sayı da sıfır değildir.")
