from data import data_tidur, id_baru
from validasi import validasi_jam, input_tanggal, input_kualitas
from tampilan import (tabel_riwayat, tabel_rata, sukses, gagal, jeda,
                      hitung_durasi)


def ambil_data(login, role):
    hasil = []
    for i in data_tidur:
        d = data_tidur[i]
        if role == "admin" or d["pemilik"] == login:
            hasil.append(i)
    return hasil


def jumlah_durasi(daftar, n):
    if n == 0:
        return 0
    return daftar[n - 1] + jumlah_durasi(daftar, n - 1)


# CREATE
def tambah_data(login):
    tanggal = input_tanggal()

    if tanggal is None:
        jeda()
        return

    waktu = []
    for label in ["tidur", "bangun"]:
        while True:
            jam = input("Jam " + label + " (HH:MM): ")

            if validasi_jam(jam):
                waktu.append(jam)
                break

            gagal("Format jam salah! Contoh: 23:30")

    kualitas = input_kualitas()

    if kualitas is not None:
        data_tidur[id_baru()] = {
            "pemilik": login,
            "tanggal": tanggal,
            "tidur": waktu[0],
            "bangun": waktu[1],
            "kualitas": kualitas
        }
        sukses("Data berhasil ditambahkan!")

    jeda()


# READ
def lihat_data(login, role):
    tampil = ambil_data(login, role)

    if len(tampil) == 0:
        gagal("Belum ada data tidur!")
    else:
        tabel_riwayat(tampil)

        daftar_durasi = []
        for i in tampil:
            daftar_durasi.append(hitung_durasi(data_tidur[i]))

        total = jumlah_durasi(daftar_durasi, len(daftar_durasi))
        rata = total // len(daftar_durasi)
        tabel_rata(rata)

    jeda()


# UPDATE
def ubah_data(login, role):
    tampil = ambil_data(login, role)

    if len(tampil) == 0:
        gagal("Belum ada data tidur.")
        jeda()
        return

    tabel_riwayat(tampil)
    pilih_data = input("Nomor data yang diubah: ")

    try:
        nomor = int(pilih_data)
        if nomor < 1 or nomor > len(tampil):
            raise ValueError
    except ValueError:
        gagal("Nomor tidak valid!")
        jeda()
        return

    d = data_tidur[tampil[nomor - 1]]

    tidur = input("Tambahkan jam tidur baru (Tekan Enter jika tetap): ")
    bangun = input("Tambahkan jam bangun baru (Tekan Enter jika tetap): ")
    kualitas = input("Kualitas baru (Tekan Enter jika tetap): ")

    salah = False

    if tidur != "" and not validasi_jam(tidur):
        gagal("Jam tidur tidak valid!")
        salah = True

    if bangun != "" and not validasi_jam(bangun):
        gagal("Jam bangun tidak valid!")
        salah = True

    if kualitas != "":
        try:
            kualitas_baru = int(kualitas)
            if kualitas_baru < 1 or kualitas_baru > 5:
                raise ValueError
        except ValueError:
            gagal("Kualitas harus angka 1 sampai 5.")
            salah = True

    if salah:
        gagal("Ada input yang tidak valid, data tidak diubah.")
    else:
        if tidur != "":
            d["tidur"] = tidur
        if bangun != "":
            d["bangun"] = bangun
        if kualitas != "":
            d["kualitas"] = int(kualitas)
        sukses("Data berhasil diubah!")

    jeda()


# DELETE
def hapus_data(login, role):
    tampil = ambil_data(login, role)

    if len(tampil) == 0:
        gagal("Belum ada data tidur!")
        jeda()
        return

    tabel_riwayat(tampil)
    pilih_data = input("Nomor data yang dihapus: ")

    try:
        nomor = int(pilih_data)
        if nomor < 1 or nomor > len(tampil):
            raise ValueError
    except ValueError:
        gagal("Nomor tidak valid!")
    else:
        yakin = input("Yakin mau hapus data? (y/n): ")

        if yakin.lower() == "y":
            data_tidur.pop(tampil[nomor - 1])
            sukses("Data berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")

    jeda()