#batas
batas = 5
for i in range(batas):
    print("Perulangan ke-", i)

nilai = [75, 60, 80, 60, 50]
for item in nilai:
    if item > 70:
        print(item, "Lulus")
else:
    print("Tidak Lulus")
print(item)

#range start, stop, step
for i in range (5, 0, -1):
    print(i)

#nested for
for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
    for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
        print(f'{i} x {j} = {i * j}')
    print('') #biar ada jarak tiap iterasi

#Perulangan while
jawab = "ya"
hitung = 0
while(jawab == "ya"):
   hitung += 1
   jawab = input("Ulang lagi tidak? ")
   
print(f"Total Perulangan : {hitung}")

#break
for i in range(10):
    if i == 5:
        break
    print(i)

#continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")

#break dan continue
for i in range(10):
    if i == 0:
        continue
    elif i == 5:
        break
    else:
        continue
    print(i)