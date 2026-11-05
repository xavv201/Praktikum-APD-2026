import pwinput
from data import akun
from tampilan import sukses, gagal, jeda


def register():
    username = input("Username baru: ")
    password = pwinput.pwinput("Password baru: ")

    ada = username in akun

    try:
        if username == "" or " " in username or len(username) < 3:
            raise ValueError("Username minimal 3 karakter tanpa spasi.")
        if ada:
            raise ValueError("Username sudah digunakan!")
        if len(password) < 4:
            raise ValueError("Password minimal 4 karakter!")
    except ValueError as e:
        gagal(str(e))
    else:
        akun[username] = {"password": password, "role": "user"}
        sukses("Register berhasil! Silakan login kembali.")
    finally:
        jeda()


def login():
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")

    for a in akun:
        if a == username and akun[a]["password"] == password:
            return a

    gagal("Username atau password salah!")
    jeda()
    return None