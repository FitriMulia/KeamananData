1. Caesar Cipher GUI (chipergui.py)
Aplikasi ini menggunakan metode Caesar Cipher untuk melakukan enkripsi dan dekripsi teks. Caesar Cipher bekerja dengan cara menggeser setiap huruf pada teks berdasarkan nilai pergeseran tertentu.

Fitur:
Masukkan teks yang akan dienkripsi atau didekripsi.
Masukkan nilai pergeseran (shift) sebagai kunci.
Hasil enkripsi atau dekripsi ditampilkan langsung.

Cara Menjalankan:
Pastikan Python dan pustaka Tkinter terpasang di komputer Anda.
Jalankan perintah:
python chipergui.py
Masukkan teks dan nilai pergeseran di antarmuka yang muncul.
Klik tombol Enkripsi untuk mengenkripsi atau Dekripsi untuk mendekripsi.


2. Data Encryption Standard GUI (desgui.py)
Aplikasi ini menggunakan algoritma Data Encryption Standard (DES) untuk melakukan enkripsi dan dekripsi teks. DES bekerja dengan kunci simetris sepanjang 8 karakter.

Fitur:
Masukkan teks dan kunci 8 karakter.
Enkripsi menghasilkan teks terenkripsi dalam format base64.
Dekripsi mengembalikan teks asli dari teks terenkripsi.
Cara Menjalankan:

Pastikan Python, pustaka Tkinter, dan pustaka PyCryptodome terpasang.
Instal PyCryptodome jika belum:
pip install pycryptodome
Jalankan perintah:
python desgui.py
Masukkan teks dan kunci, lalu klik tombol Enkripsi atau Dekripsi.


3. Enigma Cipher GUI (enigmagui.py)
Aplikasi ini mensimulasikan mesin Enigma sederhana untuk enkripsi dan dekripsi teks. Mesin Enigma menggunakan rotor untuk melakukan substitusi huruf yang berubah-ubah setiap kali teks diproses.

Fitur:
Masukkan teks yang akan dienkripsi atau didekripsi.
Rotor menggunakan konfigurasi default (misalnya, [3, 1, 4]).
Proses enkripsi dan dekripsi bekerja secara otomatis.

Cara Menjalankan:
Pastikan Python dan pustaka Tkinter terpasang.
Jalankan perintah:
python enigmagui.py
Masukkan teks di kolom input dan klik Enkripsi atau Dekripsi.


4. Steganography GUI (steganogui.py)
Aplikasi ini menggunakan teknik steganografi untuk menyembunyikan dan mengambil pesan teks dari gambar. Pesan disisipkan ke dalam gambar menggunakan algoritma Least Significant Bit (LSB).

Fitur:
Menyembunyikan pesan teks ke dalam gambar.
Mengambil pesan tersembunyi dari gambar.
Mendukung format gambar PNG dan JPG.

Cara Menjalankan:
Pastikan Python, pustaka Tkinter, dan pustaka stegano terpasang.
Instal pustaka stegano jika belum:
pip install stegano
Jalankan perintah:
python steganogui.py
Pilih gambar, masukkan pesan, lalu simpan gambar hasilnya untuk menyembunyikan pesan.
Untuk mengambil pesan, pilih gambar yang sudah disisipkan.
