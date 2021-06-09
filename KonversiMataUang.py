import os

rupiah = float(0)
dolar = float(14306.40)
yen = float(130.24)
real = float(3814.74)
hasil = float()
ulang = 'y'

os.system('cls')
print("============================")
print("Konversi Mata Uang ")
print("============================")
print("- Nama  : Aditia Jaya")
print("- NPm   : 20262011217 ")
print("- Kelas : TIK 20")

while (ulang == 'y' or ulang == 'Y'):
    print("============================")
    rupiah = float(input("Masukan Jumklah Rupiah : RP "))
    print("============================")
    print("Hasil konversi Rupiah ke : ")
    hasil = rupiah / dolar
    print("Dolar : $ " + str(hasil))
    hasil = rupiah / yen
    print("Yen   : Y " + str(hasil))
    hasil = rupiah / real
    print("Real  : R " + str(real))
    print("============================")
    ulang = input("Konversi lagi ? (y/n) :")
