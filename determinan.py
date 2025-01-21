from colorama import Fore
import pyfiglet
import numpy as num
import sys

text = pyfiglet.figlet_format("Determinan")

def det3x3():
    print("Masukkan data dibawah ini!")
    data1 = int(input("Masukkan data array ke-1: "))
    data2 = int(input("Masukkan data array ke-2: "))
    data3 = int(input("Masukkan data array ke-3: "))
    data4 = int(input("Masukkan data array ke-4: "))
    data5 = int(input("Masukkan data array ke-5: "))
    data6 = int(input("Masukkan data array ke-6: "))
    data7 = int(input("Masukkan data array ke-7: "))
    data8 = int(input("Masukkan data array ke-8: "))
    data9 = int(input("Masukkan data array ke-9: "))

    arr = num.array([[data1, data2, data3], [data4, data5, data6], [data7, data8, data9]])
    print(f"\nbentuk matriks: \n\n{arr}")

    determinan = round(num.linalg.det(arr))
    print(f"\nHasilnya: {determinan}\n")

def det2x2():
    print("Masukkan data dibawah ini!")
    data1 = int(input("Masukkan data array ke-1: "))
    data2 = int(input("Masukkan data array ke-2: "))
    data3 = int(input("Masukkan data array ke-3: "))
    data4 = int(input("Masukkan data array ke-4: "))

    arr = num.array([[data1, data2], [data3, data4]])
    print(f"\nbentuk matriks: \n\n{arr}")

    determinan = round(num.linalg.det(arr))
    print(f"\nHasilnya: {determinan}\n")

def lanjut():
    lanjut = input("Ingin melanjutkan? (y/n): ")
    lanjut.lower()

    if lanjut == "y":
        return determinan()
    elif lanjut == "n":
        print("Good bye")
        sys.exit()
    else:
        print("Input Tidak Valid")

def determinan():
    print(f"{Fore.WHITE+text} code by sultan")
    print("""
        1. Determinan 2x2
        2. Determinan 3x3
    """)
    opsi = int(input("Pilih opsi untuk melakukan operasi: "))

    if opsi == 1:
        det2x2()
    elif opsi == 2:
        det3x3()
    else:
        print("Opsi hanya tersedia (1 atau 2)")
        return determinan()

    lanjut()

determinan()
