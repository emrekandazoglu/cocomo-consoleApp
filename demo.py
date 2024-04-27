from rich.console import Console
from rich.table import Table

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

kloc = 9000 / 1000

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
