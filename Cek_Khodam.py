import random

nama = input("Masukkan nama anda: ")

khodam = [
    'Harimau Biskuat', 
    'Mulyono', 
    'Kepala pentil',
    'Babi guling',
    'Babi ngepet',
    'Spion supra',
    'Kak Gem',
    'AKM 47',
    'Tombak Moskov',
    'Jembatan Suramadu',
    'Mas Rusdi',
    'si Imut',
    ]

khodamnya = random.choice(khodam)
print(f"{nama} khodamnya adalah {khodamnya}")

