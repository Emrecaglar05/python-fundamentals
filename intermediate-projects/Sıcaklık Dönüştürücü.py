# ---------------------------
# Fonksiyon Örnekleri
# ---------------------------

# Basit toplama fonksiyonu
def topla(a, b):
    return a + b

sonuc = topla(10, 20)
print("Toplam:", sonuc)

# Dikdörtgen alan hesaplama
def dikdortgen_alani(genislik, yukseklik):
    return genislik * yukseklik

alan = dikdortgen_alani(10, 20)
print("Dikdörtgen Alanı:", alan)

# Matematiksel işlemler fonksiyonu
def matematiksel_islemler(a, b):
    toplam = a + b
    fark = a - b
    carpim = a * b
    bolum = a / b
    return toplam, fark, carpim, bolum

toplam, fark, carpim, bolum = matematiksel_islemler(10, 5)
print("Fark:", fark)


# ---------------------------
# Sıcaklık Dönüştürücü
# ---------------------------

# Dönüşüm fonksiyonları
def celcius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celcius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celcius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celcius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Menü gösterme fonksiyonu
def menu_goster():
    print("\n--- Sıcaklık Dönüştürücü Menü ---")
    print("1. Celcius → Fahrenheit & Kelvin")
    print("2. Fahrenheit → Celcius & Kelvin")
    print("3. Kelvin → Celcius & Fahrenheit")
    print("4. Çıkış")

# Ana program döngüsü
while True:
    menu_goster()
    secim = input("Seçiminizi yapın (1/2/3/4): ")

    if secim == '1':
        c = float(input("Celcius cinsinden sıcaklık girin: "))
        print(f"Fahrenheit: {celcius_to_fahrenheit(c):.2f}")
        print(f"Kelvin: {celcius_to_kelvin(c):.2f}")
    elif secim == '2':
        f = float(input("Fahrenheit cinsinden sıcaklık girin: "))
        print(f"Celcius: {fahrenheit_to_celcius(f):.2f}")
        print(f"Kelvin: {fahrenheit_to_kelvin(f):.2f}")
    elif secim == '3':
        k = float(input("Kelvin cinsinden sıcaklık girin: "))
        print(f"Celcius: {kelvin_to_celcius(k):.2f}")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(k):.2f}")
    elif secim == '4':
        print("Programdan çıkılıyor. Hoşça kalın!")
        break
    else:
        print("Geçersiz seçim. Lütfen 1-4 arasında bir seçenek girin.")
