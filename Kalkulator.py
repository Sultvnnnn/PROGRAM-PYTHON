def kalkulator():
    print('''
         === KALKULATOR SEDERHANA ===\n
          1. PERTAMBAHAN        (+)
          2. PENGURANGAN        (-)
          3. PERKALIAN          (*)
          4. PEMBAGIAN          (/)
          5. PANGKAT            (**)
          6. MODULUS            (%)
          7. FLOOR DIVISION     (//)
          
          note:
          8. Pengertian Modulus
          9. Pengertian Floor Division
          ''')
    opsi = input("Masukkan opsi yang anda inginkan: ")
    
    operator = ""
    if opsi in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if opsi == "1":
            operator = "+"
        elif opsi == "2":
            operator = "-"
        elif opsi == "3":
            operator = "*"
        elif opsi == "4":
            operator = "/"
        elif opsi == "5":
            operator = "**"
        elif opsi == "6":
            operator = "%"
        elif opsi == "7":
            operator = "//"
        elif opsi == "8":
            print("\nModulus (%): Operator ini memberikan sisa hasil bagi dari dua angka. Misalnya, `7 % 3` menghasilkan `1` karena `7` dibagi `3` menghasilkan `2` dengan sisa `1`.")
            return(kalkulator())
        elif opsi == "9":
            print("\nFloor Division (//): Operator ini membagi dua angka dan membulatkan hasilnya ke bawah (ke integer terdekat yang lebih kecil). Misalnya, `7 // 3` menghasilkan `2` karena `7` dibagi `3` adalah `2.33`, dan dibulatkan ke bawah menjadi `2`.")
            return(kalkulator())
        
        print(f"Anda memilih operator '{operator}'")
        data1 = float(input("Masukkan angka: "))
        data2 = float(input("Masukkan angka: "))
        
        if opsi == "1":
            hasil = data1 + data2
        elif opsi == "2":
            hasil = data1 - data2
        elif opsi == "3":
            hasil = data1 * data2
        elif opsi == "4":
            hasil = data1 / data2
        elif opsi == "5":
            hasil = data1 ** data2
        elif opsi == "6":
            hasil = data1 % data2
        elif opsi == "7":
            hasil = data1 // data2


# untuk cek apakah angka bersifat integer atau float
        if data1 == int(data1):
            data1 = int(data1)

        if data2 == int(data2):
            data2 = int(data2)

        if hasil == int(hasil):
            hasil = int(hasil)

        print(f"{data1} {operator} {data2} = {hasil}")
    else:
        print("OPSI YANG ANDA PILIH SALAH,\nMOHON MASUKKAN OPSI BERUPA ANGKA DENGAN BENAR :)\n")
        return(kalkulator())

kalkulator()