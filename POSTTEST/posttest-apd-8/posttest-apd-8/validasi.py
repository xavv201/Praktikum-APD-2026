from tampilan import gagal


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

        batas_hari = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

        if tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0):
            batas_hari[1] = 29

        if hari < 1 or hari > batas_hari[bulan - 1]:
            raise ValueError("Tanggal tidak valid!")
    except ValueError as e:
        gagal(str(e))
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
        gagal("Kualitas harus angka 1 sampai 5.")
        return None
    else:
        return kualitas