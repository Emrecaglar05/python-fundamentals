import time

# For döngüsü örneği (geri sayım)
for i in range(5, 0, -1):
    print(i)

# While döngüsü örneği
sayac = 0
while sayac < 5:
    print(sayac)
    sayac += 1

# For döngüsü örneği (geri sayım, 2 saniyede bir)
for i in range(10, 0, -2):
    print(i)
    time.sleep(2)
print("Mutlu Yıllar!")

# ---------------------------
# Geri Sayım Zamanlayıcı
# ---------------------------

# Adım 1: Kullanıcıdan geri sayım başlangıç değeri al
baslangic = int(input("\nGeri sayımı başlatmak için bir sayı gir: "))

# Adım 2: While döngüsü ile geri sayım
print("\n--- Geri Sayım Başlıyor ---")
while baslangic > 0:
    print(baslangic)
    time.sleep(1)
    baslangic -= 1

# Adım 3: Son mesaj
print("Geri Sayım Tamamlandı!")
