username_benar = "cici"
password_benar = "008"
pin_benar = "008008"

saldo = 5000000
daftar_menu = ["Transfer Uang", "Logout"]

login = False
for percobaan in range(3):
    print("=== LOGIN BANK DIGITAL ===")
    username = input("Masukkan Username anda: ")
    password = input("Masukkan Password anda: ")

    if username == username_benar and password == password_benar:
        login = True
        print("Login berhasil!\n")
        break

    if username != username_benar and password != password_benar:
        print("Username dan Password anda salah. Silakan coba lagi.")
    elif username != username_benar:
        print("Username anda salah")
    else:
        print("Password anda salah")
    print(f"Sisa kesempatan: {2 - percobaan}\n")

if not login:
    print("Akun Anda diblokir. Silakan hubungi customer service.")
else:

    while True:
        print("=== MENU UTAMA ===")
        for i in range(len(daftar_menu)):
            print(f"{i + 1}. {daftar_menu[i]}")
        pilihan = input("Pilih menu: ")

        if pilihan != "1" and pilihan != "2":
            print("Pilihan tidak valid!\n")
            continue

        if pilihan == "2":
            print("Logout berhasil. Terima kasih!")
            break

        blokir = False
        while True:
            print(f"\nSaldo saat ini   : Rp{saldo},00")
            penerima = input("Username penerima: ")

            while True:
                nominal = int(input("Nominal transfer : Rp"))
                if nominal < 50000:
                    print("Nominal minimal Rp50.000,00")
                    continue
                if nominal > 1000000:
                    print("Nominal maksimal Rp1.000.000,00")
                    continue
                if nominal > saldo:
                    print("Saldo anda tidak mencukupi")
                    continue
                break

            pin_valid = False
            for percobaan_pin in range(3):
                pin = input("Masukkan PIN     : ")
                if pin == pin_benar:
                    pin_valid = True
                    break
                print(f"PIN salah! Sisa kesempatan: {2 - percobaan_pin}")

            if not pin_valid:
                print("PIN salah 3x. Akun Anda diblokir.")
                blokir = True
                break

            saldo -= nominal
            print("\n===== STRUK TRANSFER =====")
            print(f"Pengirim  : {username_benar}")
            print(f"Penerima  : {penerima}")
            print(f"Nominal   : Rp{nominal},00")
            print("==========================\n")
            print("Dana berhasil dikirim ke penerima!\n")

            lagi = input("Apakah ingin transfer lagi (y/n)? ")
            while lagi != "y" and lagi != "n":
                print("Masukkan y atau n saja")
                lagi = input("Apakah ingin transfer lagi (y/n)? ")
            if lagi == "n":
                break

        if blokir:
            break