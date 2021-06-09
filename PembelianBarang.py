import os

ulang = str('y')
history = str()
jumlah_barang = int()
harga_barang = int()
nama_barang = str()
total_barang = int()
total_belanja = int()
eror = 0

os.system('cls')
print("============================")
print("Aplikasi penjualan ")
print("============================")
print("- Nama  : Aditia Jaya")
print("- NPm   : 20262011217 ")
print("- Kelas : TIK 20")
print("============================")
nik = input("NIK        :")
nama = input("Nama       :")
no_telepon = input("No Telepon :")
while ulang == 'y':
    print("============================")
    print("Menu :")
    print(" 1  Minyak Goreng : Rp 12000")
    print(" 2  Kopi          : Rp 3500")
    print(" 3  Susu          : Rp 5000")
    print(" 4  Roko          : Rp 20000")
    print(" 5  Tepung Terigu : Rp 7500")
    print(" 6  Margarin      : Rp 12500")
    print(" 7  Telor         : Rp 9000")
    print(" 8  Tisu          : RP 2500")
    print(" 9  Sabun         : Rp 3000")
    print(" 10 Shampo        : Rp 1500")
    print("============================")
    menu = int(input("Silahkan Pilih Barang : "))
    if (menu == 1):
        harga_barang = 12000
        nama_barang = "Minyak Goreng : Rp 12000"
    elif (menu == 2):
        harga_barang = 3500
        nama_barang = "Kopi          : Rp 3500"
    elif (menu == 3):
        harga_barang = 5000
        nama_barang = "Susu          : Rp 5000"
    elif (menu == 4):
        harga_barang = 20000
        nama_barang = "Roko          : Rp 20000"
    elif (menu == 5):
        harga_barang = 7500
        nama_barang = "Tepung Terigu : Rp 7500"
    elif (menu == 6):
        harga_barang = 12500
        nama_barang = "Margarin      : Rp 12500"
    elif (menu == 7):
        harga_barang = 9000
        nama_barang = "Telor         : Rp 9000"
    elif (menu == 8):
        harga_barang = 2500
        nama_barang = "Tisu          : RP 2500"
    elif (menu == 9):
        harga_barang = 3000
        nama_barang = "Sabun         : Rp 3000"
    elif (menu == 10):
        harga_barang = 5000
        nama_barang = "Shampo        : Rp 1500"
    else:
        print("Input Salah, Silahkan Coba Lagi")
        eror = 1
        break

    jumlah_barang = int(input("Jumlah Barang : "))
    total_barang = jumlah_barang * harga_barang
    history = history + "\n" + nama_barang + " (" + str(jumlah_barang) + ") Rp. " + str(total_barang)
    total_belanja = total_belanja + total_barang

    beli = input("Ingin Beli Lagi ? (y/n)")
    if (beli == 'y' or beli == 'Y'):
        print("")
    else:
        break
if (eror != 1):
    print(history)
    print("============================")
    print("Total belanja :              Rp. " + str(total_belanja))
    print("============================")