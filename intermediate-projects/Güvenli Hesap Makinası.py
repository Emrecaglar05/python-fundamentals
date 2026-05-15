# Hata Yakalama ve Güvenli Hesap Makinesi

# --- Örnek 1: Basit try-except ---
try:
    sayi = int(input("Bir sayı giriniz: "))
    sonuc = 10 / sayi
    print("Sonuç:", sonuc)
except ZeroDivisionError:
    print("Hata: Sıfıra bölme yapılamaz.")
except ValueError:
    print("Hata: Geçersiz giriş. Lütfen bir sayı giriniz.")

# --- Örnek 2: try-except-else-finally ---
try:
    sayi = int(input("Bir sayı giriniz: "))
    sonuc = 10 / sayi
except ZeroDivisionError:
    print("Hata: Sıfıra bölme yapılamaz.")
else:
    print("Hata oluşmadı. Sonuç:", sonuc)
finally:
    print("Program sonlandı (finally bloğu çalıştı).")

# --- Örnek 3: Birden fazla hata yakalama ---
try:
    sayi = int(input("Bir sayı giriniz: "))
    sonuc = 10 / sayi
except (ZeroDivisionError, ValueError):
    print("Hata: Sıfıra bölme ya da geçersiz giriş.")

# --- raise örneği ---
def para_cek(miktar):
    if miktar < 0:
        raise ValueError("Geçersiz işlem: Para miktarı negatif olamaz.")
    print(f"{miktar} TL başarıyla çekildi.")

try:
    para_cek(-50)
except ValueError as hata:
    print("Hata:", hata)

# --- Güvenli Hesap Makinesi ---

# 1. Adım: İşlem Fonksiyonları
def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    if y == 0:
        raise ZeroDivisionError("Sıfıra bölme yapılamaz")
    return x / y

# 2. Adım: Menü Gösterme
def menu_goster():
    print("\n--- Güvenli Hesap Makinesi ---")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

# 3. Adım: Ana Program Döngüsü
while True:
    menu_goster()
    secim = input("Seçiminizi giriniz (1-5): ")

    if secim == '5':
        print("Hesap makinesi kapatılıyor... Hoşçakalın!")
        break

    try:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))

        if secim == '1':
            print("Sonuç:", topla(sayi1, sayi2))
        elif secim == '2':
            print("Sonuç:", cikar(sayi1, sayi2))
        elif secim == '3':
            print("Sonuç:", carp(sayi1, sayi2))
        elif secim == '4':
            print("Sonuç:", bol(sayi1, sayi2))
        else:
            print("Geçersiz seçim. Lütfen 1-5 arasında bir değer giriniz.")

    except ValueError:
        print("Hata: Geçersiz giriş. Lütfen sayı giriniz.")
    except ZeroDivisionError as hata:
        print("Hata:", hata)
    except Exception as hata:
        print("Beklenmeyen bir hata oluştu:", hata)
    finally:
        print("Hesap makinesini kullandığınız için teşekkürler!... Yeniden başlatılıyor...")
