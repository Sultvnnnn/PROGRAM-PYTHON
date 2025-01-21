# DATE AND TIME
import datetime as dt

print("="*35 + "\n")

print("Silahkan masukkan data dibawah ini: ")
tanggal = int(input("Tanggal \t\t: "))
bulan = int(input("Bulan \t\t\t: "))
tahun = int(input("Tahun \t\t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print("-"*35 + "\n")
print(f"Tanggal lahir kamu\t: ({tanggal_lahir})")
print(f"Hari \t\t\t: {tanggal_lahir:%A}")
print(f"Bulan \t\t\t: {tanggal_lahir:%B}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"Umur anda dalam hari\t: {umur_hari}")
print(f"Umur anda dalam tahun \t: {umur_tahun} tahun")

print("\n"+ "="*35)