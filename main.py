import os
import sys

# Jalur aman penemu folder modul di HP/Pydroid 3
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Memanggil DB Helper untuk Login/Register & Riwayat
from db_helper import daftar_user, login_user, simpan_riwayat, lihat_riwayat

# Memanggil seluruh fungsi dari kedua modul (geometri huruf kecil)
from geometri import *
from cek_angka import *

user_aktif = None

def portal_akses():
    global user_aktif
    while True:
        print("\n========================================")
        print("   SYSTEM PORTAL (LOGIN / REGISTER)    ")
        print("========================================")
        print("1. Login Akun")
        print("2. Registrasi Akun Baru")
        print("3. Keluar / Exit")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            print("\n--- LOGIN AKUN ---")
            identifier = input("Email / Username : ")
            pwd = input("Password         : ")
            status, username_res, pesan = login_user(identifier, pwd)
            print(f"-> {pesan}")
            if status:
                user_aktif = username_res
                break
                
        elif pilihan == "2":
            print("\n--- REGISTRASI AKUN BARU ---")
            email = input("Email Baru    : ")
            uname = input("Username Baru : ")
            pwd = input("Password Baru : ")
            status, pesan = daftar_user(email, uname, pwd)
            print(f"-> {pesan}")
            
        elif pilihan == "3":
            print("\nProgram dihentikan. Sampai jumpa!")
            sys.exit()
        else:
            print("\nPilihan tidak valid, silakan coba lagi.")

def main():
    portal_akses()
    
    while True:
        print("\n========================================")
        print(f" MODUL MATEMATIKA | Akun: {user_aktif.upper()}")
        print("========================================")
        print("1. Hitung Luas Persegi")
        print("2. Hitung Keliling Persegi")
        print("3. Cek Bilangan Prima")
        print("4. Cek Bilangan Genap / Ganjil")
        print("5. Hitung Luas Lingkaran")
        print("6. Hitung Luas Segitiga")
        print("7. Lihat Riwayat Tersimpan")
        print("8. Logout & Keluar")
        print("========================================")
        
        pilihan = input("Pilih menu (1-8): ")
        
        if pilihan == "1":
            print("\n--- MODUL 1: LUAS PERSEGI ---")
            sisi = float(input("Masukkan sisi: "))
            hasil = luas_persegi(sisi)
            print(f"-> Hasil Luas Persegi: {hasil}")
            simpan_riwayat(user_aktif, "Luas Persegi", hasil)
            
        elif pilihan == "2":
            print("\n--- MODUL 2: KELILING PERSEGI ---")
            sisi = float(input("Masukkan sisi: "))
            hasil = keliling_persegi(sisi)
            print(f"-> Hasil Keliling Persegi: {hasil}")
            simpan_riwayat(user_aktif, "Keliling Persegi", hasil)
            
        elif pilihan == "3":
            print("\n--- MODUL 3: BILANGAN PRIMA ---")
            angka = int(input("Masukkan angka: "))
            status_p = is_prima(angka)
            teks = "Bilangan Prima" if status_p else "BUKAN Bilangan Prima"
            print(f"-> {angka} adalah {teks}.")
            simpan_riwayat(user_aktif, "Cek Prima", f"{angka} ({teks})")
                
        elif pilihan == "4":
            print("\n--- MODUL 4: GENAP / GANJIL ---")
            x = int(input("Masukkan angka: "))
            hasil = status_genap_ganjil(x)
            print(f"-> {x} adalah {hasil}.")
            simpan_riwayat(user_aktif, "Ganjil Genap", f"{x} ({hasil})")
                
        elif pilihan == "5":
            print("\n--- MODUL 5: LUAS LINGKARAN ---")
            r = float(input("Masukkan jari-jari: "))
            hasil = luas_lingkaran(r)
            print(f"-> Hasil Luas Lingkaran: {hasil}")
            simpan_riwayat(user_aktif, "Luas Lingkaran", hasil)

        elif pilihan == "6":
            print("\n--- MODUL 6: LUAS SEGITIGA ---")
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            hasil = luas_segitiga(alas, tinggi)
            print(f"-> Hasil Luas Segitiga: {hasil}")
            simpan_riwayat(user_aktif, "Luas Segitiga", hasil)
            
        elif pilihan == "7":
            print(f"\n--- RIWAYAT TERSIMPAN [{user_aktif}] ---")
            print(lihat_riwayat(user_aktif))

        elif pilihan == "8":
            print(f"\nBerhasil logout dari akun {user_aktif}. Terima kasih!")
            break
        else:
            print("\nPilihan salah, masukkan angka 1 sampai 8.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
