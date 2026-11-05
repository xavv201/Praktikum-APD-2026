akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "xavv": {"password": "xavv201", "role": "user"}
}

data_tidur = {
    1: {"pemilik": "xavv", "tanggal": "10-10-2026", "tidur": "23:00", "bangun": "05:00", "kualitas": 4},
    2: {"pemilik": "xavv", "tanggal": "11-10-2026", "tidur": "02:30", "bangun": "05:49", "kualitas": 3}
}


def id_baru():
    if len(data_tidur) == 0:
        return 1
    return max(data_tidur) + 1