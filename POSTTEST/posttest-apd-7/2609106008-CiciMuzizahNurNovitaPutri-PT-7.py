import os

akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "xavv": {"password": "xavv201", "role": "user"}
}

data_tidur = {
    1: {"pemilik": "xavv", "tanggal": "10-10-2026", "tidur": "23:00", "bangun": "05:00", "kualitas": 4},
    2: {"pemilik": "xavv", "tanggal": "11-10-2026", "tidur": "02:30", "bangun": "05:49", "kualitas": 3}
}

id_berikut = 3 

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_data(d, durasi):
    print("\nTanggal:", d["tanggal"])
    print("Pemilik:", d["pemilik"])
    print("Jam tidur:", d["tidur"])
    print("Jam bangun:", d["bangun"])
    print("Durasi:", durasi // 60, "jam",
          durasi % 60, "menit")
    print("Kualitas:", d["kualitas"], "/5")

def validasi_jam(jam):
    try:
        if len(jam) != 5 or jam[2] != ":":
            raise ValueError("Format jam harus HH:MM")
        if not jam[:2].isdigit() or not jam[3:].isdigit():
            raise ValueError("Jam dan menit harus angka")
        if int(jam[:2]) > 23 or int(jam[3:]) > 59:
            raise ValueError("Jam atau menit di luar batas!")
    except ValueError:
        return False
    else: 
        return True 


def jumlah_durasi(daftar, n):
    if n == 0:
        return 0
    return daftar[n - 1] + jumlah_durasi(daftar, n - 1)


def input_tanggal():
    tanggal = input("Tanggal (DD-MM-YYYY): ")

    try:
        if (len(tanggal) != 10 or tanggal[2] != "-"
            or tanggal[5] != "-"
            or not tanggal[:2].isdigit()
            or not tanggal[3:5].isdigit()
            or not tanggal[6:].isdigit()):
            raise ValueError("Format tanggal salah! Contoh: 20-09-2026")

        hari = int(tanggal[:2])
        bulan = int(tanggal[3:5])
        tahun = int(tanggal[6:])

        if bulan < 1 or bulan > 12:
            raise ValueError("Bulan tidak valid!")

        batas_hari = [31, 28, 31, 30, 31, 30,           # batas hari tiap bulan (dari januari-desember)
                      31, 31, 30, 31, 30, 31]

        if tahun % 400 == 0 or (                        # mmeriksa apakah termasuk tahun kabisat atau tidak
            tahun % 4 == 0 and tahun % 100 != 0
        ):
            batas_hari[1] = 29

        if hari < 1 or hari > batas_hari[bulan - 1]:
            raise ValueError("Tanggal tidak valid!")
    except ValueError as e:
        print(e)
        return None
    else:
        return tanggal


def input_kualitas():
    kualitas = input("Kualitas tidur (1-5): ")

    try:
        kualitas = int(kualitas)
        if kualitas < 1 or kualitas > 5:
            raise ValueError
    except ValueError:
        print("Kualitas harus angka 1 sampai 5.")
        return None
    else:
        return kualitas

while True:
    bersihkan_layar()
    print("=== PENCATAT WAKTU TIDUR ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "3":
        print("Program selesai.")
        break

    elif pilih == "2":
        username = input("Username baru: ")
        password = input("Password baru: ")

        ada = False
        for a in akun:
            if a == username:
                ada = True

        try:
            if username == "" or " " in username or len(username) < 3:
                raise ValueError("Username minimal 3 karakter tanpa spasi.")
            if ada:
                raise ValueError("Username sudah digunakan!")
            if len(password) < 4:
                raise ValueError("Password minimal 4 karakter!")
        except ValueError as e:
            print(e)
        else:
            akun[username] = {"password": password, "role": "user"}
            print("Register berhasil! Silakan login kembali.")
        finally:
            input("Tekan Enter untuk lanjut.")

    elif pilih == "1":
        username = input("Username: ")
        password = input("Password: ")

        login = None
        for a in akun:
            if a == username and akun[a]["password"] == password:
                login = a

        if login is None:
            print("Username atau password salah!")
            input("Tekan Enter untuk lanjut.")
            continue

        role = akun[login]["role"]

        while True:
            bersihkan_layar()
            print("=== MENU", login, "-", role, "===")
            print("1. Tambah data tidur")
            print("2. Lihat riwayat tidur")
            print("3. Ubah data tidur")
            print("4. Hapus data tidur")

            if role == "admin":
                print("5. Lihat daftar akun")

            print("0. Logout")
            menu = input("Pilih menu: ")

            # CREATE
            if menu == "1":
                tanggal = input_tanggal()

                if tanggal is None:
                    input("Tekan Enter.")
                    continue

                waktu = []
                for label in ["tidur", "bangun"]:
                    while True:
                        jam = input("Jam " + label + " (HH:MM): ")

                        if validasi_jam(jam):
                            waktu.append(jam)
                            break

                        print("Format jam salah! Contoh: 23:30")

                kualitas = input_kualitas()

                if kualitas is not None:
                    data_tidur[id_berikut] = {
                        "pemilik": login,
                        "tanggal": tanggal,
                        "tidur": waktu[0],
                        "bangun": waktu[1],
                        "kualitas": kualitas
                    }
                    id_berikut = id_berikut + 1
                    print("Data berhasil ditambahkan!")

                input("Tekan Enter untuk lanjut.")

            # READ
            elif menu == "2":
                daftar_durasi = []

                for i in data_tidur:
                    d = data_tidur[i]
                    if role == "admin" or d["pemilik"] == login:
                        mulai = int(d["tidur"][:2]) * 60 + int(d["tidur"][3:])
                        akhir = int(d["bangun"][:2]) * 60 + int(d["bangun"][3:])
                        durasi = akhir - mulai

                        if durasi <= 0:
                            durasi = durasi + 1440

                        tampilkan_data(d, durasi)
                        daftar_durasi.append(durasi)

                if len(daftar_durasi) == 0:
                    print("Belum ada data tidur!")
                else:
                    total = jumlah_durasi(daftar_durasi, len(daftar_durasi))
                    rata = total // len(daftar_durasi)
                    print("\nRata-rata durasi tidur:",
                          rata // 60, "jam", rata % 60, "menit")

                input("Tekan Enter untuk lanjut.")

            # UPDATE
            elif menu == "3":
                tampil = []

                for i in data_tidur:
                    d = data_tidur[i]
                    if role == "admin" or d["pemilik"] == login:
                        tampil.append(i)

                if len(tampil) == 0:
                    print("Belum ada data tidur.")
                    input("Tekan Enter.")
                    continue

                for no in range(len(tampil)):
                    d = data_tidur[tampil[no]]
                    print(no + 1, d["pemilik"], d["tanggal"], d["tidur"], d["bangun"],
                          "Kualitas:", d["kualitas"])

                pilih_data = input("Nomor data yang diubah: ")

                try:
                    nomor = int(pilih_data)
                    if nomor < 1 or nomor > len(tampil):
                        raise ValueError
                except ValueError:
                    print("Nomor tidak valid!")
                    input("Tekan Enter.")
                    continue

                d = data_tidur[tampil[nomor - 1]]

                tidur = input("Tambahkan jam tidur baru (Tekan Enter jika tetap): ")
                bangun = input("Tambahkan jam bangun baru (Tekan Enter jika tetap): ")
                kualitas = input("Kualitas baru (Tekan Enter jika tetap): ")

                salah = False

                if tidur != "":
                    if not validasi_jam(tidur):
                        print("Jam tidur tidak valid!")
                        salah = True

                if bangun != "":
                    if not validasi_jam(bangun):
                        print("Jam bangun tidak valid!")
                        salah = True

                if kualitas != "":
                    try:
                        kualitas_baru = int(kualitas)
                        if kualitas_baru < 1 or kualitas_baru > 5:
                            raise ValueError
                    except ValueError:
                        print("Kualitas harus angka 1 sampai 5.")
                        salah = True

                if salah:
                    print("Ada input yang tidak valid, data tidak diubah.")
                else:
                    if tidur != "":
                        d["tidur"] = tidur
                    if bangun != "":
                        d["bangun"] = bangun
                    if kualitas != "":
                        d["kualitas"] = int(kualitas)
                    print("Data berhasil diubah!")

                input("Tekan Enter untuk lanjut.")

            # DELETE
            elif menu == "4":
                tampil = []

                for i in data_tidur:
                    d = data_tidur[i]
                    if role == "admin" or d["pemilik"] == login:
                        tampil.append(i)

                if len(tampil) == 0:
                    print("Belum ada data tidur!")
                    input("Tekan Enter.")
                    continue

                for no in range(len(tampil)):
                    d = data_tidur[tampil[no]]
                    print(no + 1, d["pemilik"], d["tanggal"], d["tidur"], d["bangun"],
                          "Kualitas:", d["kualitas"])

                pilih_data = input("Nomor data yang dihapus: ")

                try:
                    nomor = int(pilih_data)
                    if nomor < 1 or nomor > len(tampil):
                        raise ValueError
                except ValueError:
                    print("Nomor tidak valid!")
                else:
                    yakin = input("Yakin mau hapus data? (y/n): ")

                    if yakin.lower() == "y":
                        data_tidur.pop(tampil[nomor - 1])
                        print("Data berhasil dihapus!")
                    else:
                        print("Penghapusan dibatalkan.")

                input("Tekan Enter untuk lanjut.")

            # MENU ADMIN
            elif menu == "5" and role == "admin":
                for a in akun:
                    print(a, "-", akun[a]["role"])

                input("Tekan Enter untuk lanjut.")

            elif menu == "0":
                break

            else:
                print("Menu tidak valid!")
                input("Tekan Enter untuk lanjut.")

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut.")