# ---------------------------
# Demetler ve Kümeler
# ---------------------------

# Demet örnekleri
koordinatlar = (10, 20, 30)
x, y, z = koordinatlar
print("X:", x)
print("Y:", y)
print("Z:", z)

meyveler = ("elma", "muz", "kiraz")
print("Meyve sayısı:", len(meyveler))

# Yeni bir meyve ekleyerek yeni demet oluşturma
yeni_meyveler = meyveler + ("portakal",)
print("Güncellenmiş meyveler:", yeni_meyveler)

# Küme örnekleri
malzemeler = {"un", "şeker", "tereyağı"}
print("Başlangıç malzemeleri:", malzemeler)

malzemeler.add("yumurta")
print("Yeni malzemeler:", malzemeler)

malzemeler.remove("şeker")
print("Şeker çıkarıldıktan sonra:", malzemeler)

# Kümelerle işlemler
set_a = {"un", "şeker", "tereyağı"}
set_b = {"şeker", "yumurta"}

print("Birleşim (union):", set_a | set_b)
print("Kesişim (intersection):", set_a & set_b)
print("Fark (difference):", set_a - set_b)


# ---------------------------
# Malzeme Kontrol Uygulaması
# ---------------------------

# 1. Adım: Tarif için gereken malzemeler
tarif_malzemeleri = {"un", "şeker", "tereyağı", "yumurta", "süt"}

# 2. Adım: Kullanıcıdan sahip olduğu malzemeleri al
kullanici_girdisi = input("Sahip olduğunuz malzemeleri girin (virgülle ayrılmış): ")
kullanici_malzemeleri = set(kullanici_girdisi.split(", "))

# 3. Adım: Eksik ve fazla malzemeleri bul
eksik_malzemeler = tarif_malzemeleri - kullanici_malzemeleri
fazla_malzemeler = kullanici_malzemeleri - tarif_malzemeleri

# 4. Adım: Sonuçları göster
print("\n--- Malzeme Kontrol Sonuçları ---")
if eksik_malzemeler:
    print(f"Eksik malzemeler: {', '.join(eksik_malzemeler)}")
else:
    print("Tüm gerekli malzemelere sahipsiniz.")

if fazla_malzemeler:
    print(f"Fazladan malzemeler: {', '.join(fazla_malzemeler)}")
else:
    print("Fazladan malzemeniz yok.")
