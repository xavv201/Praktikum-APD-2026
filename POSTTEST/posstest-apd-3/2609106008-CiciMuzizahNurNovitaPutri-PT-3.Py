nama = input("Masukkan Nama Anda: ")
umur = int(input("Masukkan Umur Anda: "))

print("\nDaftar Harga Tiket yang Tersedia:")
print("1. Reguler - Rp 50.000")
print("2. Premium - Rp 75.000")
print("3. VIP     - Rp 100.000")
jenis_tiket = input("\nMasukkan Jenis Tiket yang Anda Pilih, ketik persis seperti contoh (Reguler/Premium/VIP): ")
status_member = input("Apakah Anda Member? (Ya/Tidak): ")
nominal_bayar = int(input("Masukkan Nominal Bayar Anda   : "))

if umur < 13:
    print("Mohon maaf, Anda belum cukup umur untuk menonton.")
else:
    if jenis_tiket != "Reguler" and jenis_tiket != "Premium" and jenis_tiket != "VIP":
        print("\nJenis tiket yang Anda masukkan tidak valid. Transaksi dibatalkan.")
    else:
        if jenis_tiket == "Reguler":
            harga_tiket = 50000
        elif jenis_tiket == "Premium":
            harga_tiket = 75000
        elif jenis_tiket == "VIP":
            harga_tiket = 100000

        diskon_persen = 0.2 if status_member == "Ya" else 0
        nominal_diskon = harga_tiket * diskon_persen
        biaya_admin = 0 if status_member == "Ya" else 2000
        total_bayar = harga_tiket - nominal_diskon + biaya_admin

        if nominal_bayar < total_bayar:
            print("\nUang yang Anda Masukkan Kurang. Transaksi dibatalkan.")
        else:
            kembalian = nominal_bayar - total_bayar
            print("\nTransaksi berhasil!")
            print("Nama Anda    :", nama)
            print("Umur Anda    :", umur)
            print("Jenis Tiket  :", jenis_tiket)
            print("Status Member:", status_member)
            print("Harga Tiket  : Rp", harga_tiket)
            print("Diskon       : Rp", nominal_diskon)
            print("Biaya Admin  : Rp", biaya_admin)
            print("Total Bayar  : Rp", total_bayar)
            print("Nominal Bayar: Rp", nominal_bayar)
            print("Kembalian    : Rp", kembalian)