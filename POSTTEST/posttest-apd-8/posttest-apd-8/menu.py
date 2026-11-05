import autent
import crud
from data import akun
from tampilan import bersihkan_layar, tampil_menu, tabel_akun, gagal, jeda


def menu_user(login, role):
    while True:
        bersihkan_layar()

        pilihan = [
            ("1", "Tambah data tidur"),
            ("2", "Lihat riwayat tidur"),
            ("3", "Ubah data tidur"),
            ("4", "Hapus data tidur")
        ]

        if role == "admin":
            pilihan.append(("5", "Lihat daftar akun"))

        pilihan.append(("0", "Logout"))

        tampil_menu("MENU " + login + " - " + role, pilihan)
        menu = input("Pilih menu: ")

        if menu == "1":
            crud.tambah_data(login)
        elif menu == "2":
            crud.lihat_data(login, role)
        elif menu == "3":
            crud.ubah_data(login, role)
        elif menu == "4":
            crud.hapus_data(login, role)
        elif menu == "5" and role == "admin":
            tabel_akun()
            jeda()
        elif menu == "0":
            break
        else:
            gagal("Menu tidak valid!")
            jeda()


def menu_utama():
    while True:
        bersihkan_layar()
        tampil_menu("PENCATAT WAKTU TIDUR", [
            ("1", "Login"),
            ("2", "Register"),
            ("3", "Keluar")
        ])
        pilih = input("Pilih menu: ")

        if pilih == "3":
            print("Program selesai.")
            break
        elif pilih == "2":
            autent.register()
        elif pilih == "1":
            login = autent.login()
            if login is not None:
                menu_user(login, akun[login]["role"])
        else:
            gagal("Pilihan tidak valid!")
            jeda()