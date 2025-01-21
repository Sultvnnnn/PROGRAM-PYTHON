print("\n === KONVERSI SUHU === \n")

def celcius_fahrenheit(celcius):
    return(celcius * 9/5) + 32

def fahrenheit_celcius(fahrenheit):
    return(fahrenheit - 32) * 5/9

def celcius_kelvin(celcius):
    return(celcius +  273)

def kelvin_celcius(kelvin):
    return(kelvin - 273)

def fahrenheit_kelvin(fahrenheit):
    return(fahrenheit + 459) * 5/9

def kelvin_fahrenheit(kelvin):
    return(kelvin * 9/5) - 459

def konversi_suhu():
    print("Pilih opsi yg ingin digunakan:")
    print("1. CELCIUS     -> FAHRENHEIT")
    print("2. FAHRENHEIT  -> CELCIUS")
    print("3. CELCIUS     -> KELVIN")
    print("4. KELVIN      -> CELCIUS")
    print("5. FAHRENHEIT  -> KELVIN")
    print("6. KELVIN      -> FAHRENHEIT")

    choice = input("Ketikkan angka: ")
    if choice == "1":
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        print(f"{celcius}°C to Fahrenheit = {celcius_fahrenheit(celcius)}°F")
    elif choice == "2":
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        print(f"{fahrenheit}°F to Celcius = {fahrenheit_celcius(fahrenheit)}°C")
    elif choice == "3":
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        print(f"{celcius}°C to Kelvin = {celcius_kelvin(celcius)}°K")
    elif choice == "4":
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        print(f"{kelvin}°K to Celcius = {kelvin_celcius(kelvin)}°C")
    elif choice == "5":
        fahrenheit = float(input("Masukkan suhu dalam Kelvin: "))
        print(f"{fahrenheit}°F to Kelvin = {fahrenheit_kelvin(fahrenheit)}°K")
    elif choice == "6":
        kelvin = float(input("Masukkan suhu dalam Fahrenheit: "))
        print(f"{kelvin}°K to Fahrenheit = {kelvin_fahrenheit(kelvin)}°F")
    else:
        print("Opsi error, mohon masukkan angka dengan benar\n")
        return(konversi_suhu())

konversi_suhu()