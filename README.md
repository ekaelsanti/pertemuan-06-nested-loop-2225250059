# Pertemuan 06 Nested Loop Python

**Nama:** Eka Elsanti  
**NIM:** 2225250059  
**Kelas:** 3A  

---

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan untuk menyelesaikan masalah dua dimensi, membentuk pola, serta mengolah pasangan data secara terstruktur.

---

## Cara Menjalankan
Jalankan perintah berikut di terminal:
```bash
python3 tugas/tabel_perkalian_dan_statistik.py

```

---

## Algoritma Tugas 3

1. Membaca input `n` bertipe integer positif dan melakukan validasi berulang dengan `while` jika `n <= 0`.
2. Menginisialisasi variabel `total_semua = 0` dan `count_genap = 0` sebelum perulangan.
3. Perulangan luar (`for i in range(1, n + 1)`) mengendalikan baris dan menginisialisasi `total_baris = 0` di awal setiap baris.
4. Perulangan dalam (`for j in range(1, n + 1)`) menghitung `hasil = i * j`, menampilkan hasil perkalian, serta menambahkan `hasil` ke `total_baris` dan `total_semua`.
5. Jika `hasil % 2 == 0`, variabel `count_genap` bertambah 1.
6. Menampilkan `total_baris` setelah perulangan dalam selesai.
7. Menampilkan `total_semua` dan `count_genap` setelah seluruh perulangan selesai.

---

## Hasil Pengujian

| n | Jumlah Pasangan | Total Diharapkan | Total Aktual | Genap Diharapkan | Genap Aktual | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 0 | 0 | Sesuai |
| 2 | 4 | 9 | 9 | 3 | 3 | Sesuai |
| 3 | 9 | 36 | 36 | 5 | 5 | Sesuai |

---

## Analisis Efisiensi

Badan loop dalam dieksekusi sebanyak $n \times n$ ($n^2$) kali. Untuk nilai $n = 1$ dieksekusi 1 kali, $n = 2$ dieksekusi 4 kali, dan $n = 3$ dieksekusi 9 kali. Kompleksitas waktu program ini adalah $O(n^2)$.

---

## Refleksi

Kesalahan umum pada nested loop adalah menempatkan akumulator per baris (`total_baris`) di luar perulangan luar atau lupa meresetnya ke 0 di setiap baris baru. Hal ini menyebabkan nilai baris sebelumnya ikut terjumlahkan ke baris berikutnya. Penempatan `total_baris = 0` di dalam perulangan luar sebelum perulangan dalam memastikan perhitungan per baris selalu dimulai dari awal secara akurat.