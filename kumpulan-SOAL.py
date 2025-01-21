"""
Soal no 1 
Buat sebuah program berdasarkan input pengguna untuk menentukan bilangan ganjil atau genap
"""
def ganjilgenap():
    data = int(input("Masukkan Angka: "))
    if data % 2 == 0:
        print("genap")
    else:
        print("ganjil")

ganjilgenap()

print("\n")

"""
Soal no 2
Buat sebuah program untuk menentukan kelulusan berdasarkan nilai. jika nilai >= 75 lulus, jika nilai antara 50 dan 74 remedial,
dan jika nilai kurang dari 50 maka tidak lulus
"""
def kelulusan():
    nilai = int(input("Masukkan nilai: "))

    if nilai >= 75:
        print("Lulus")
    
    elif 50 <= nilai <= 74:
        print("remedial")

    else:
        print("tidak lulus")
kelulusan()

print("\n")

"""
Soal no 3
Buat sebuah program untuk menentukan diskon belanja. jika total belanja lebih dari 1.000.000 dapat diskon 10%, 
jika belanja antara 500.000 dan 1.000.000 dapat diskon 5%, dan jika belanja dibawah 500.000 tidak dapat diskon. hitung dan
tampilan total yang harus dibayar setelah diskon
"""
def belanja():
    harga_awal = int(input("Masukkan total harga belanja: Rp. "))

    if harga_awal >= 1000000:
        print("Selamat anda dapat diskon 10%")
        harga_kedua = harga_awal * 0.1
        total_harga = harga_awal - harga_kedua
        print(f"Total belanja anda setelah diskon menjadi Rp. {total_harga}")        

    elif 500000 <= harga_awal <= 1000000:
        print("Selamat anda dapat diskon 5%")
        harga_kedua = harga_awal * 0.05
        total_harga = harga_awal - harga_kedua
        print(f"Total belanja anda setelah diskon menjadi Rp. {total_harga}")

    else:
        print(f"Total belanja anda adalah {harga_awal}")
belanja()
