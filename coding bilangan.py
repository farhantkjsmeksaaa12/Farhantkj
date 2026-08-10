while True:
    print("\n--- Program Cek Ganjil Genap ---")
    x_input = input("Masukkan Nilai X (atau ketik 'keluar' untuk berhenti): ")
    
    # Kondisi untuk menghentikan perulangan
    if x_input.lower() == 'keluar':
        print("Program selesai. Terima kasih!")
        break
        
    # Validasi dan eksekusi logika angka
    try:
        x = int(x_input)
        if x % 2 == 0:
            print(f"Bilangan {x} termasuk Bilangan genap")
        else:
            print(f"Bilangan {x} termasuk Bilangan ganjil")
    except ValueError:
        print("Input tidak valid! Silakan masukkan angka bulat atau ketik 'keluar'.")
