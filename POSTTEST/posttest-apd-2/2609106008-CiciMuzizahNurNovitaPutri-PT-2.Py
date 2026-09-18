barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000 
barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]

total_belanja = barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6
pajak = total_belanja * 0.15
total_bayar = total_belanja + pajak

rata_rata = total_bayar / len(barang)

nim = 8
boolean = nim < rata_rata

kurs_usd = 17818
kurs_rub = 211.69
total_bayar_usd = total_bayar / kurs_usd
total_bayar_rub = total_bayar / kurs_rub

slicing_barang = barang[0:5:2]

print("harga barang 1: Rp", barang_1)
print("harga barang 2: Rp", barang_2)
print("harga barang 3: Rp", barang_3)
print("harga barang 4: Rp", barang_4)
print("harga barang 5: Rp", barang_5)
print("harga barang 6: Rp", barang_6)
print("Daftar harga barang:", barang)
print("Total belanjaan: Rp", total_belanja)
print("Pajak (15%): Rp", pajak)
print("Total bayar: Rp", total_bayar)
print("Rata-rata harga: Rp", rata_rata)
print("Apakah NIM lebih kecil dari rata-rata harga?", boolean)
print("Total bayar dalam USD: $", total_bayar_usd)
print("Total bayar dalam RUB: ₽", total_bayar_rub)
print("List Slicing (barang 1, 3, 5):", slicing_barang)