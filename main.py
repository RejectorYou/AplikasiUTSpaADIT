import os

print("Menu Aplikasi : \n")
print("1. Pembelian Barang")
print("2. Konversi Mata Uang")

app = int(input("\nPilih aplikasi yang akan di jalankan : "))

if (app == 1):
    os.system('python PembelianBarang.py')
elif (app == 2):
    os.system('python KonversiMataUang.py')
else:
    print("Input Salah, Silahkan Coba Lagi")
