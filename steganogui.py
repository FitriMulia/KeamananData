import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb

def sembunyikan_pesan():
    try:
        img_path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("PNG Files", "*.png"), ("JPG Files", "*.jpg")])
        if not img_path:
            return

        pesan = entry_pesan.get()
        if not pesan:
            messagebox.showerror("Error", "Pesan tidak boleh kosong")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".png", title="Simpan Gambar", filetypes=[("PNG Files", "*.png")])
        if not save_path:
            return

        secret_image = lsb.hide(img_path, pesan)
        secret_image.save(save_path)
        messagebox.showinfo("Sukses", f"Pesan berhasil disembunyikan ke {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyembunyikan pesan: {e}")

def tampilkan_pesan():
    try:
        img_path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("PNG Files", "*.png"), ("JPG Files", "*.jpg")])
        if not img_path:
            return

        pesan = lsb.reveal(img_path)
        if pesan:
            entry_hasil.delete(0, tk.END)
            entry_hasil.insert(0, pesan)
        else:
            messagebox.showinfo("Info", "Tidak ada pesan yang tersembunyi di gambar ini")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menampilkan pesan: {e}")

# Membuat GUI
window = tk.Tk()
window.title("Steganography")
window.geometry("500x300")

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

# Gradient background
bg_label = tk.Label(window)
apply_gradient(bg_label, "#aec6cf", "#cfcfc4")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label dan Entry untuk pesan
label_pesan = tk.Label(window, text="Pesan untuk Disembunyikan:", bg="#aec6cf", fg="black")
label_pesan.pack(pady=5)
entry_pesan = tk.Entry(window, width=50)
entry_pesan.pack(pady=5)

# Tombol untuk menyembunyikan pesan
button_hide = tk.Button(window, text="Sembunyikan Pesan", command=sembunyikan_pesan, bg="#cfcfc4", fg="black")
button_hide.pack(pady=10)

# Tombol untuk menampilkan pesan
button_reveal = tk.Button(window, text="Tampilkan Pesan", command=tampilkan_pesan, bg="#cfcfc4", fg="black")
button_reveal.pack(pady=10)

# Entry untuk hasil
label_hasil = tk.Label(window, text="Pesan Tersembunyi:", bg="#aec6cf", fg="black")
label_hasil.pack(pady=5)
entry_hasil = tk.Entry(window, width=50)
entry_hasil.pack(pady=5)

# Menjalankan GUI
window.mainloop()
