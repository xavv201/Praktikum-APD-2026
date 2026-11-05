import os
from prettytable import PrettyTable
from colorama import Fore, init
from data import data_tidur, akun

init(autoreset=True)


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def sukses(teks):
    print(Fore.GREEN + teks)


def gagal(teks):
    print(Fore.RED + teks)


def jeda():
    input("Tekan Enter untuk lanjut.")


def hitung_durasi(d):
    mulai = int(d["tidur"][:2]) * 60 + int(d["tidur"][3:])
    akhir = int(d["bangun"][:2]) * 60 + int(d["bangun"][3:])
    durasi = akhir - mulai

    if durasi <= 0:
        durasi = durasi + 1440
    return durasi


def format_durasi(menit):
    return str(menit // 60) + " jam " + str(menit % 60) + " menit"


def tampil_menu(judul, pilihan):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = ["Kode", "Menu"]
    tabel.align["Menu"] = "l"

    for kode, teks in pilihan:
        tabel.add_row([kode, teks])

    print(tabel)


def tabel_riwayat(daftar_id):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Pemilik", "Tanggal", "Jam Tidur",
                         "Jam Bangun", "Durasi", "Kualitas"]

    for no in range(len(daftar_id)):
        d = data_tidur[daftar_id[no]]
        tabel.add_row([
            no + 1,
            d["pemilik"],
            d["tanggal"],
            d["tidur"],
            d["bangun"],
            format_durasi(hitung_durasi(d)),
            str(d["kualitas"]) + "/5"
        ])

    print(tabel)


def tabel_rata(rata):
    tabel = PrettyTable()
    tabel.field_names = ["Keterangan", "Hasil"]
    tabel.add_row(["Rata-rata durasi tidur", format_durasi(rata)])
    print(tabel)


def tabel_akun():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Username", "Role"]

    no = 1
    for a in akun:
        tabel.add_row([no, a, akun[a]["role"]])
        no = no + 1

    print(tabel)