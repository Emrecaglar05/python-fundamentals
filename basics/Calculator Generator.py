isim = input("Adını gir: ")
print(f"Merhaba, {isim}")

sayi1 = int(input("Bir sayı gir: "))
sayi1 = str(sayi1)
print(f"Sayı ikiyle çarpıldı: {sayi1 * 2}")

sayi1 = int(input("Birinci sayıyı gir: "))
sayi2 = int(input("İkinci sayıyı gir: "))
sonuc = sayi1 + sayi2

print(f"{sayi1} ve {sayi2} toplamı = {sonuc}")

a = 5
b = 3

print(f"Toplama: {a + b}")
print(f"Çıkarma: {a - b}")
print(f"Çarpma: {a * b}")
print(f"Bölme: {a / b}")
print(f"Tamsayı Bölme: {a // b}")
print(f"Mod (kalan): {a % b}")
print(f"Üs Alma: {a ** b}")

# Basit Hesap Makinesi

# Adım 1: Kullanıcıdan iki sayı al
sayi1 = float(input("Birinci sayıyı gir: "))
sayi2 = float(input("İkinci sayıyı gir: "))

# Adım 2: Dört işlem yap
toplama = sayi1 + sayi2
cikarma = sayi1 - sayi2
carpma = sayi1 * sayi2
bolme = sayi1 / sayi2 if sayi2 != 0 else "Sıfıra bölme yapılamaz"

# Adım 3: Sonuçları göster
print("\n--- Hesap Makinesi Sonuçları ----")
print(f"Toplama: {sayi1} + {sayi2} = {toplama}")
print(f"Çıkarma: {sayi1} - {sayi2} = {cikarma}")
print(f"Çarpma: {sayi1} x {sayi2} = {carpma}")
print(f"Bölme: {sayi1} / {sayi2} = {bolme}")
