# cek_angka.py (Modul untuk Pengecekan Angka)
import math

def is_prima(n):
    """Mengecek apakah n merupakan bilangan prima"""
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def status_genap_ganjil(x):
    """Mengecek apakah x ganjil atau genap"""
    if x % 2 == 0:
        return "Bilangan Genap"
    else:
        return "Bilangan Ganjil"
      
