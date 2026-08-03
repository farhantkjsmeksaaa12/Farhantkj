# Program Menghitung Dua Bilangan Sederhana

# 1. Mengambil input angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# 2. Melakukan operasi aritmatika
penjumlahan = angka1 + angka2
pengurangan = angka1 - angka2
perkalian   = angka1 * angka2

# Pembagian dengan penanganan agar tidak error saat dibagi 0
if angka2 != 0:
    pembagian = angka1 / angka2
else:
    pembagian = "Tidak bisa dibagi dengan nol (0)"

# 3. Menampilkan hasil perhitungan
print("\n--- HASIL PERHITUNGAN ---")
print(f"Hasil Penjumlahan ({angka1} + {angka2}) : {penjumlahan}")
print(f"Hasil Pengurangan ({angka1} - {angka2}) : {pengurangan}")
print(f"Hasil Perkalian   ({angka1} * {angka2}) : {perkalian}")
print(f"Hasil Pembagian   ({angka1} / {angka2}) : {pembagian}")