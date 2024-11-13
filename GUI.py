import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    try:
        # Memeriksa setiap input nilai mata pelajaran
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        # Menampilkan hasil prediksi
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError:
        # Menampilkan pesan kesalahan jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#FFB6C1")

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Italic", 10, "bold"), bg="#FFB6C1")
judul_label.pack(pady=20)

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#FFB6C1")
frame_input.pack(pady=10)

# Membuat list untuk menyimpan entry nilai mata pelajaran
entries = []
for i in range(10):
    # Label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Italic", 10, "bold"), bg="#FFB6C1")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    # Entry untuk setiap mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Italic", 10))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Tombol untuk memproses hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Italic", 10, "bold"), bg="#f0f0f0")
prediksi_button.pack(pady=30)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Italic", 10, "italic", "bold"), fg="red", bg="#f0f0f0")
hasil_label.pack(pady=20)

# Menjalankan loop utama aplikasi
root.mainloop()
