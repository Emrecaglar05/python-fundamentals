# Basit Fonksiyon Örnekleri

def fonksiyon_adi():
    # Fonksiyon içindeki kod bloğu
    print("Fonksiyondan merhaba")

fonksiyon_adi()

def selamla():
    print("Merhaba, Python'a hoş geldin!")

selamla()

def kullaniciyi_selamla(isim):
    print(f"Merhaba, {isim}! Python'a hoş geldin!")

kullaniciyi_selamla('Emre')

def topla(a, b):
    print(f"Toplam: {a + b}")

topla(5, 4)

def carp(a, b):
    return a * b

sonuc = carp(5, 4)
print("Çarpım sonucu: ", sonuc)

# -------------------------------
# Basit Matematik Quiz Oyunu
# -------------------------------

import random

# Adım 1: Soru üretme fonksiyonu
def soru_uret():
    sayi1 = random.randint(1, 10)
    sayi2 = random.randint(1, 10)
    islem = random.choice(['+', '-', '*'])

    if islem == '+':
        cevap = sayi1 + sayi2
    elif islem == '-':
        cevap = sayi1 - sayi2
    else:
        cevap = sayi1 * sayi2

    return f"{sayi1} {islem} {sayi2}", cevap

# Adım 2: Ana quiz oyunu fonksiyonu
def matematik_quiz():
    puan = 0
    tur_sayisi = 5

    print("\n--- Matematik Quiz Oyununa Hoş Geldin! ---")
    print("Sana matematik soruları sorulacak, doğru cevapları vermelisin.")

    for i in range(tur_sayisi):
        soru, dogru_cevap = soru_uret()
        print(f"\nSoru {i + 1}: {soru}")
        kullanici_cevap = int(input("Cevabın: "))

        if kullanici_cevap == dogru_cevap:
            print("Doğru! 🎉")
            puan += 1
        else:
            print(f"Yanlış ❌ Doğru cevap: {dogru_cevap}")

    print("\n--- Oyun Bitti! ---")
    print(f"Sonucun: {puan}/{tur_sayisi}")
    if puan == tur_sayisi:
        print("Tebrikler! Tüm soruları doğru bildin 🏆")
    elif puan >= tur_sayisi // 2:
        print("Güzel iş çıkardın 👏")
    else:
        print("Daha çok pratik yapmalısın, tekrar dene! 💪")

# Adım 3: Oyunu çalıştır
matematik_quiz()
