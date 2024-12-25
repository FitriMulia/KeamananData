import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def enkripsi(plain_text, key):
    try:
        cipher = DES.new(key, DES.MODE_ECB)
        padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
        encrypted_text = cipher.encrypt(padded_text)
        return base64.b64encode(encrypted_text).decode('utf-8')
    except Exception as e:
        messagebox.showerror("Error", f"Enkripsi gagal: {e}")

def dekripsi(encrypted_text, key):
    try:
        cipher = DES.new(key, DES.MODE_ECB)
        decoded_text = base64.b64decode(encrypted_text)
        decrypted_text = unpad(cipher.decrypt(decoded_text), DES.block_size)
        return decrypted_text.decode('utf-8')
    except Exception as e:
        messagebox.showerror("Error", f"Dekripsi gagal: {e}")

def proses_enkripsi():
    plain_text = entry_plain.get()
    key = entry_key.get().encode('utf-8')

    if len(key) != 8:
        messagebox.showerror("Error", "Kunci harus 8 karakter")
        return

    hasil = enkripsi(plain_text, key)
    entry_hasil.delete(0, tk.END)
    entry_hasil.insert(0, hasil)

def proses_dekripsi():
    encrypted_text = entry_plain.get()
    key = entry_key.get().encode('utf-8')

    if len(key) != 8:
        messagebox.showerror("Error", "Kunci harus 8 karakter")
        return

    hasil = dekripsi(encrypted_text, key)
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
window.title("DES Encryption")
window.geometry("400x300")


bg_label = tk.Label(window)
apply_gradient(bg_label, "#ffc0cb", "#f5deb3")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label dan Entry untuk teks asli
label_plain = tk.Label(window, text="Teks Asli / Terenkripsi:", bg="#ffc0cb", fg="black")
label_plain.pack(pady=5)
entry_plain = tk.Entry(window, width=50)
entry_plain.pack(pady=5)

# Label dan Entry untuk kunci
label_key = tk.Label(window, text="Kunci (8 karakter):", bg="#ffc0cb", fg="black")
label_key.pack(pady=5)
entry_key = tk.Entry(window, width=20)
entry_key.pack(pady=5)

# Tombol Enkripsi
button_encrypt = tk.Button(window, text="Enkripsi", command=proses_enkripsi, bg="#f5deb3", fg="black")
button_encrypt.pack(pady=5)

# Tombol Dekripsi
button_decrypt = tk.Button(window, text="Dekripsi", command=proses_dekripsi, bg="#f5deb3", fg="black")
button_decrypt.pack(pady=5)

# Entry untuk hasil
label_hasil = tk.Label(window, text="Hasil:", bg="#ffc0cb", fg="black")
label_hasil.pack(pady=5)
entry_hasil = tk.Entry(window, width=50)
entry_hasil.pack(pady=5)

# Menjalankan GUI
window.mainloop()
