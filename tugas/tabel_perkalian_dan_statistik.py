# Program Tabel Perkalian dan Statistik
print("Tabel Perkalian dan Statistik")

# 1. Validasi input n (harus positif)
n = int(input("n: "))
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# 2. Inisialisasi total keseluruhan dan counter genap
total_semua = 0
count_genap = 0

# 3. Nested loop untuk tabel, total baris, total semua, dan hitung genap
for i in range(1, n + 1):
    total_baris = 0
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")
        total_baris += hasil
        total_semua += hasil
        if hasil % 2 == 0:
            count_genap += 1
    print(f" | Jumlah baris = {total_baris}")

# 4. Tampilkan statistik akhir
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")