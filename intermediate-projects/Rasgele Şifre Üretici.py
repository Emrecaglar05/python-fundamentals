# ---------------------------
# Matematik ve Rastgele Modüller
# ---------------------------
import math
import random
import string
import os
import datetime

# Kareköklü örnek
print("16'nın karekökü:", math.sqrt(16))

# 1-10 arasında rastgele sayı
print("Rastgele sayı (1-10):", random.randint(1, 10))

# Rastgele seçim
meyveler = ["Elma", "Muz", "Kiraz"]
print("Rastgele meyve seçimi:", random.choices(meyveler))

# Rastgele parola oluşturma
def parola_uret(uzunluk=12):
    if uzunluk < 4:
        raise ValueError("Parola uzunluğu en az 4 karakter olmalıdır.")

    # Karakter kümeleri
    buyuk_harfler = string.ascii_uppercase
    kucuk_harfler = string.ascii_lowercase
    sayilar = string.digits
    ozel_karakterler = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    # Her karakter tipinden en az bir tane
    parola = [
        random.choice(buyuk_harfler),
        random.choice(kucuk_harfler),
        random.choice(sayilar),
        random.choice(ozel_karakterler)
    ]

    # Kalan karakterleri rastgele doldur
    tum_karakterler = buyuk_harfler + kucuk_harfler + sayilar + ozel_karakterler
    parola += random.choices(tum_karakterler, k=uzunluk - 4)

    # Karakterleri karıştır
    random.shuffle(parola)

    # Listeyi stringe çevir ve döndür
    return ''.join(parola)

# Kullanıcıdan parola uzunluğu alma ve parola oluşturma
try:
    uzunluk = int(input("Oluşturulacak parolanın uzunluğunu girin (minimum 4): "))
    parola = parola_uret(uzunluk)
    print("Oluşturulan parola:", parola)
except ValueError as e:
    print("Hata:", e)
