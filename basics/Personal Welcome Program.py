# Bir ismi değişkende saklama
isim = "Emre"
kisiIsmi = "Emre"

# Yaşı değişkende saklama
yas = 42

# String
isim = "Emre"

# Integer (tam sayı)
yas = 21

# Float (ondalıklı sayı)
boy = 5.8

# Boolean (doğru/yanlış)
ogrenci_mi = True

print(type(isim))
print(type(yas))
print(type(boy))
print(type(ogrenci_mi))

yas = "42"

benimYasim = int(yas)

print(benimYasim + 5)

isim = "Emre"

print("Merhaba, " + isim + "!")

print("Merhaba Dostum, {}!".format(isim))

print(f"Merhaba, {isim}!")

# Kişiselleştirilmiş Karşılama Programı

# Adım 1: Kullanıcı bilgilerini sor
isim = input("Adın nedir? ")
yas = int(input("Kaç yaşındasın? "))
renk = input("En sevdiğin renk nedir? ")

# Adım 2: Kişiselleştirilmiş mesaj üret
print("\n---- Kişiselleştirilmiş Karşılama ----")
print(f"Merhaba, {isim}! 👋")
print(f"{yas} yaşındasın ve {renk} gerçekten güzel bir renk!")
print("Artık Python macerana hazırsın 🚀🐍")
