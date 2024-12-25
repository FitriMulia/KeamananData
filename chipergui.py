import tkinter as tk
from tkinter import messagebox

def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def proses_enkripsi():
    plain_text = entry_plain.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Error", "Pergeseran harus berupa angka")
        return

    hasil = enkripsi(plain_text, shift)
    entry_hasil.delete(0, tk.END)
    entry_hasil.insert(0, hasil)

def proses_dekripsi():
    cipher_text = entry_plain.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Error", "Pergeseran harus berupa angka")
        return

    hasil = dekripsi(cipher_text, shift)
    entry_hasil.delete(0, tk.END)
    entry_hasil.insert(0, hasil)

def apply_gradient(widget, color1, color2):
    width = widget.winfo_screenwidth()
    height = widget.winfo_screenheight()
    gradient = tk.PhotoImage(width=width, height=height)

    for y in range(height):
        r = int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * y // height
        g = int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * y // height
        b = int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * y // height
        color = f"#{r:02x}{g:02x}{b:02x}"
        gradient.put(color, to=(0, y, width, y + 1))

    widget.config(image=gradient)
    widget.image = gradient

# Membuat GUI
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("400x250")

# Membuat gradasi background
bg_label = tk.Label(window)
apply_gradient(bg_label, "#f5deb3", "#8b4513")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label dan Entry untuk teks asli
label_plain = tk.Label(window, text="Teks Asli / Terenkripsi:", bg="#f5deb3", fg="black")
label_plain.pack(pady=5)
entry_plain = tk.Entry(window, width=50)
entry_plain.pack(pady=5)

# Label dan Entry untuk pergeseran
label_shift = tk.Label(window, text="Pergeseran (Shift):", bg="#f5deb3", fg="black")
label_shift.pack(pady=5)
entry_shift = tk.Entry(window, width=20)
entry_shift.pack(pady=5)

# Tombol Enkripsi
button_encrypt = tk.Button(window, text="Enkripsi", command=proses_enkripsi, bg="#8b4513", fg="white")
button_encrypt.pack(pady=5)

# Tombol Dekripsi
button_decrypt = tk.Button(window, text="Dekripsi", command=proses_dekripsi, bg="#8b4513", fg="white")
button_decrypt.pack(pady=5)

# Entry untuk hasil
label_hasil = tk.Label(window, text="Hasil:", bg="#f5deb3", fg="black")
label_hasil.pack(pady=5)
entry_hasil = tk.Entry(window, width=50)
entry_hasil.pack(pady=5)

# Menjalankan GUI
window.mainloop()
