from rich.console import Console
from rich.table import Table

table = Table(title="Ayarlanmamıs islev Nokta AIN sayısı")
rows = [
    ["Kullanıcı Girdi sayısı", "3", "4", "6"],
    ["Kullanıcı cikti sayısı", "4", "5", "7"],
    ["Kullanıcı sorgu sayısı", "3", "4", "6"],
    ["kutuk sayısı", "7", "10", "15"],
    ["dissal arayuz sayısı", "5", "7", "10"],
]
columns = ["parametreler", "yalin", "orta", "karisik"]

for column in columns:
    table.add_column(column)

for row in rows:
    table.add_row(*row, style="bright_green")

console = Console()
console.print(table)


kgs = input("Kullanıcı Girdi sayısıni gir")
tkgs = input("tabloya gore deger giriniz")
kcs = input("Kullanıcı cikti sayısıni gir")
tkcs = input("tabloya gore deger giriniz")
kss = input("Kullanıcı sorgu sayısıni gir")
tkss = input("tabloya gore deger giriniz")
ks = input("kutuk sayısını gir")
tks = input("tabloya gore deger giriniz")
das = input("dissal arayuz sayısını gir")
tdas = input("tabloya gore deger giriniz")

ain = (
    int(kgs) * int(tkgs)
    + int(kcs) * int(tkcs)
    + int(kss) * int(tkss)
    + int(ks) * int(tks)
    + int(das) * int(tdas)
)

print("Toplam: ", ain)

print("-----------------------------------------------------------")
print("TKF hesaplama")
print("her maddeye 0 den 5 e kadar puan veriniz")

table = Table(title="Teknik Karmaşıklık Faktörü (TKF)")
rows1 = [
    [
        "Uygulama, güvenilir yedekleme ve kurtarma gerektiriyor mu?",
        "0 dan 5 e kadar puan veriniz",
    ],
    ["Veri iletişimi gerektiriyor mu?", "0 dan 5 e kadar puan veriniz"],
    ["Dağıtılmış İşlemler var mı?", "0 dan 5 e kadar puan veriniz"],
    ["Performans kritik mi?", "0 dan 5 e kadar puan veriniz"],
    [
        "Girdiler, çıktılar, dosyalar ya da sorgular karmaşık mı?",
        "0 dan 5 e kadar puan veriniz",
    ],
    ["İçsel işlemler karmaşık mı?", "0 dan 5 e kadar puan veriniz"],
    ["Tasarlanacak kod yeniden kullanılabilir mi?", "0 dan 5 e kadar puan veriniz"],
    [
        "Dönüştürme ve kurulun tasarımda dikkate alınacak mı?",
        "0 dan 5 e kadar puan veriniz",
    ],
]
columns1 = ["parametreler", "puan"]

for column in columns1:
    table.add_column(column)

for row in rows1:
    table.add_row(*row, style="bright_green")

console = Console()
console.print(table)
tkf1 = input("Uygulama, güvenilir yedekleme ve kurtarma gerektiriyor mu?")
tkf2 = input("Veri iletişimi gerektiriyor mu?")
tkf3 = input("Dağıtılmış İşlemler var mı?")
tkf4 = input("Performans kritik mi?")
tkf5 = input("Girdiler, çıktılar, dosyalar ya da sorgular karmaşık mı?")
tkf6 = input("İçsel işlemler karmaşık mı?")
tkf7 = input("Tasarlanacak kod yeniden kullanılabilir mi?")
tkf8 = input("Dönüştürme ve kurulun tasarımda dikkate alınacak mı?")

tkf = (
    int(tkf1)
    + int(tkf2)
    + int(tkf3)
    + int(tkf4)
    + int(tkf5)
    + int(tkf6)
    + int(tkf7)
    + int(tkf8)
)


in_ = ain * (0.65 + 0.01 * tkf)


# Tabloyu oluşturma
table = Table(title="Programlama Dili Faktörü")
rows = [
    ["1", "Assembly", "300"],
    ["2", "COBOL", "100"],
    ["3", "Fortran", "100"],
    ["4", "Pascal", "90"],
    ["5", "C", "90"],
    ["6", "Ada", "70"],
    ["7", "Nesne Kıkenli Diller", "30"],
    ["8", "4. Kuşak Diller", "20"],
    ["9", "Kod Üreticiler", "15"],
]
columns = ["Sıra", "Dil", "Puan"]

for column in columns:
    table.add_column(column)

for row in rows:
    table.add_row(*row, style="bright_green")

console = Console()
console.print(table)

# Kullanıcıdan dil sırasını alma
dil_sirasi = int(input("Programlama dilinin sırasını giriniz: "))

# Sıraya göre puanı alma
puan = None
satirSayisi = 0
for row in rows:
    if int(row[0]) == dil_sirasi:
        puan = row[2]
        break

if puan is not None:
    satirSayisi = in_ * int(puan)
    print("Satır Sayısı: ", satirSayisi)

else:
    print("Belirtilen sırada bir programlama dili bulunamadı.")


print("-----------------------------------------------------------")
print("COCOMO")
print("TEMEL MODEL")

print("COCOMO")
a_ayrik = 2.4
b_ayrik = 1.05
c_ayrik = 2.5
d_ayrik = 0.38
a_yarigomulu = 3.0
b_yarigomulu = 1.12
c_yarigomulu = 2.5
d_yarigomulu = 0.35
a_karisik = 3.6
b_karisik = 1.20
c_karisik = 2.5
d_karisik = 0.32

kloc = satirSayisi / 1000
print("KLOC: ", kloc)

table = Table(title="TABLO")
rows = [
    ["Ayrik", str(a_ayrik), str(b_ayrik), str(c_ayrik), str(d_ayrik)],
    [
        "Yarıgömülü",
        str(a_yarigomulu),
        str(b_yarigomulu),
        str(c_yarigomulu),
        str(d_yarigomulu),
    ],
    ["Karisik", str(a_karisik), str(b_karisik), str(c_karisik), str(d_karisik)],
]
columns = ["TIP", "a", "b", "c", "d"]

for column in columns:
    table.add_column(column)

for row in rows:
    table.add_row(*row, style="bright_green")

console = Console()
console.print(table)

ayrik_is_gucu = a_ayrik * (kloc**b_ayrik)
ayrik_zaman = c_ayrik * (ayrik_is_gucu**d_ayrik)
ayrik_ortalama = ayrik_is_gucu / ayrik_zaman
ayrik_verimlilik = ayrik_is_gucu / kloc

yarigomulu_is_gucu = a_yarigomulu * (kloc**b_yarigomulu)
yarigomulu_zaman = c_yarigomulu * (yarigomulu_is_gucu**d_yarigomulu)
yarigomulu_ortalama = yarigomulu_is_gucu / yarigomulu_zaman
yarigomulu_verimlilik = yarigomulu_is_gucu / kloc

karisik_is_gucu = a_karisik * (kloc**b_karisik)
karisik_zaman = c_karisik * (karisik_is_gucu**d_karisik)
karisik_ortalama = karisik_is_gucu / karisik_zaman
karisik_verimlilik = karisik_is_gucu / kloc

print("-----------------------------------------------------------")
table = Table(title="COCOMO")

rows = [
    [
        "Ayrik",
        str(ayrik_is_gucu),
        str(ayrik_zaman),
        str(ayrik_ortalama),
        str(ayrik_verimlilik),
    ],
    [
        "Yarıgömülü",
        str(yarigomulu_is_gucu),
        str(yarigomulu_zaman),
        str(yarigomulu_ortalama),
        str(yarigomulu_verimlilik),
    ],
    [
        "Karisik",
        str(karisik_is_gucu),
        str(karisik_zaman),
        str(karisik_ortalama),
        str(karisik_verimlilik),
    ],
]

columns = ["TIP", "İş Gücü", "Zaman", "Ortalama", "Verimlilik"]

for column in columns:
    table.add_column(column)

for row in rows:
    table.add_row(*row, style="bright_green")

console.print(table)


print("-----------------------------------------------------------")
print("COCOMO ara model")

print("is gücü hesaplama")
K_ayrik = 3.2 * (kloc**1.05)
K_yarigomulu = 3.0 * (kloc**1.12)
K_karisik = 2.8 * (kloc**1.20)


# Maliyet etmenlerini ve değerlerini tanımlama


maliyet_etmenleri = [
    "RELY",
    "DATA",
    "CPLX",
    "TIME",
    "STOR",
    "VIRT",
    "TURN",
    "ACAP",
    "AEXP",
    "PCAP",
    "VEXP",
    "LEXP",
    "MODP",
    "TOOL",
    "SCED",
]

columns = [
    "Maliyet Etmeni",
    "Çok Düşük",
    "Düşük",
    "Normal",
    "Yüksek",
    "Çok Yüksek",
    "Oldukça Yüksek",
]

degerler = [
    [0.75, 0.88, 1.00, 1.15, 1.40, "-"],
    ["-", 0.94, 1.00, 1.08, 1.16, "-"],
    [0.70, 0.85, 1.00, 1.15, 1.30, 1.65],
    ["-", "-", 1.00, 1.11, 1.30, 1.66],
    ["-", "-", 1.00, 1.06, 1.21, 1.56],
    ["-", 0.87, 1.00, 1.15, 1.30, "-"],
    ["-", 0.87, 1.00, 1.07, 1.15, "-"],
    [1.46, 1.19, 1.00, 0.86, 0.71, "-"],
    [1.29, 1.13, 1.00, 0.91, 0.82, "-"],
    [1.42, 1.17, 1.00, 0.86, 0.70, "-"],
    [1.21, 1.10, 1.00, 0.90, "-", "-"],
    [1.14, 1.07, 1.00, 0.95, "-", "-"],
    [1.24, 1.10, 1.00, 0.91, 0.82, "-"],
    [1.24, 1.10, 1.00, 0.91, 0.83, "-"],
    [1.23, 1.08, 1.00, 1.04, 1.10, "-"],
]

# Tabloyu oluşturma
table = Table(title="Maliyet Çarpanı Tablosu", show_header=True)

# Sütunları ekleme
for column in columns:
    table.add_column(column, justify="center")

# Satırları ekleme
for i, etmen in enumerate(maliyet_etmenleri):
    row = [etmen]
    for deger in degerler[i]:
        if deger != "-":
            row.append(str(deger))
        else:
            row.append("-")
    table.add_row(*row)

# Tabloyu yazdırma
console = Console()
console.print(table)

# EAF değeri için başlangıç değeri


# Kullanıcıdan her satır için bir veri alarak hesaplamayı yapma
eaf_degeri = 1
for i, etmen in enumerate(maliyet_etmenleri):
    veri = input(f"Lütfen '{etmen}' için bir veri girin (veya '-' girerek atla): ")
    if veri != "-":
        try:
            veri = float(veri)
            if veri < 0:
                raise ValueError("Negatif değer giremezsiniz.")
            eaf_degeri *= veri
        except ValueError:
            print("Geçersiz bir değer girdiniz. Lütfen pozitif bir sayı girin.")

print("EAF Değeri:", eaf_degeri)


print("-----------------------------------------------------------")
print("duzeltilmis is gucu hesaplama")
ayrik_duzeltilmis = K_ayrik * eaf_degeri
yarigomulu_duzeltilmis = K_yarigomulu * eaf_degeri
karisik_duzeltilmis = K_karisik * eaf_degeri

print("Ayrik Düzeltimli İş Gücü:", ayrik_duzeltilmis)
print("Yarıgömülü Düzeltimli İş Gücü:", yarigomulu_duzeltilmis)
print("Karisik Düzeltimli İş Gücü:", karisik_duzeltilmis)
