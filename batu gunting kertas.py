import tkinter as tk
import random

# Fungsi untuk menentukan pemenang
def determine_winner(player_choice):
    choices = ['Batu', 'Gunting', 'Kertas']
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = "Seri!"
    elif (player_choice == "Batu" and computer_choice == "Gunting") or \
         (player_choice == "Gunting" and computer_choice == "Kertas") or \
         (player_choice == "Kertas" and computer_choice == "Batu"):
        result = f"Kamu menang! Komputer memilih {computer_choice}."
    else:
        result = f"Kamu kalah! Komputer memilih {computer_choice}."

    label_result.config(text=result)

# Fungsi untuk menangani klik tombol
def player_chooses_batu():
    determine_winner('Batu')

def player_chooses_gunting():
    determine_winner('Gunting')

def player_chooses_kertas():
    determine_winner('Kertas')

# Membuat jendela utama
root = tk.Tk()
root.title("Game Batu Gunting Kertas")

# Label judul
label_title = tk.Label(root, text="Pilih Batu, Gunting, atau Kertas", font=("Helvetica", 16))
label_title.pack(pady=20)

# Tombol untuk pilihan pemain
button_batu = tk.Button(root, text="Batu", width=15, command=player_chooses_batu)
button_batu.pack(pady=5)

button_gunting = tk.Button(root, text="Gunting", width=15, command=player_chooses_gunting)
button_gunting.pack(pady=5)

button_kertas = tk.Button(root, text="Kertas", width=15, command=player_chooses_kertas)
button_kertas.pack(pady=5)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="", font=("Helvetica", 14))
label_result.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
