Berikut adalah README yang menjelaskan tentang kode aplikasi pengolahan gambar yang Anda berikan:

---

# Image Enhancement Application

## Deskripsi
Aplikasi **Image Enhancement** ini adalah alat sederhana berbasis GUI (Graphical User Interface) yang dibuat dengan Python menggunakan Tkinter dan OpenCV. Aplikasi ini memungkinkan pengguna untuk melakukan peningkatan dan pengolahan gambar seperti peningkatan kontras, peningkatan ketajaman, reduksi noise, dan penyesuaian kecerahan pada gambar yang dimuat.

## Fitur
- **Load Image**: Memuat gambar dari penyimpanan lokal untuk diproses lebih lanjut.
- **Save Image**: Menyimpan gambar hasil pengolahan ke penyimpanan lokal.
- **Reset Image**: Mengembalikan gambar ke kondisi aslinya sebelum diproses.
- **Enhance Contrast**: Meningkatkan kontras gambar menggunakan metode histogram equalization.
- **Enhance Sharpness**: Meningkatkan ketajaman gambar menggunakan filter konvolusi.
- **Reduce Noise**: Mengurangi noise pada gambar menggunakan metode Non-Local Means Denoising.
- **Adjust Brightness**: Mengatur kecerahan gambar menggunakan slider.

## Cara Menggunakan
1. **Memuat Gambar**: Klik tombol **Load Image** untuk memilih gambar dari penyimpanan lokal.
2. **Menyimpan Gambar**: Setelah melakukan pengolahan, klik tombol **Save Image** untuk menyimpan hasilnya.
3. **Mereset Gambar**: Untuk mengembalikan gambar ke kondisi asli, klik tombol **Reset Image**.
4. **Peningkatan Kontras**: Klik tombol **Enhance Contrast** untuk meningkatkan kontras gambar.
5. **Peningkatan Ketajaman**: Klik tombol **Enhance Sharpness** untuk meningkatkan ketajaman gambar.
6. **Reduksi Noise**: Klik tombol **Reduce Noise** untuk mengurangi noise pada gambar.
7. **Penyesuaian Kecerahan**: Gunakan slider **Adjust Brightness** untuk mengatur kecerahan gambar.

## Prasyarat
- Python 3.x
- Pustaka Python yang dibutuhkan:
  - OpenCV (`opencv-python`)
  - Tkinter (biasanya sudah terinstal bersama Python)
  - Pillow (`Pillow`)

## Instalasi
1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/image-enhancement-app.git
   ```
2. **Instal Dependensi**:
   ```bash
   pip install opencv-python Pillow
   ```

3. **Jalankan Aplikasi**:
   ```bash
   python app.py
   ```

## Struktur Kode
- `load_image()`: Memuat gambar dari penyimpanan lokal dan menampilkannya di GUI.
- `save_image()`: Menyimpan gambar hasil pengolahan ke penyimpanan lokal.
- `display_image(image)`: Menampilkan gambar di GUI.
- `reset_image()`: Mengembalikan gambar ke kondisi aslinya.
- `enhance_contrast()`: Meningkatkan kontras gambar menggunakan metode histogram equalization.
- `enhance_sharpness()`: Meningkatkan ketajaman gambar menggunakan filter konvolusi.
- `reduce_noise()`: Mengurangi noise pada gambar menggunakan metode Non-Local Means Denoising.
- `adjust_brightness(value)`: Mengatur kecerahan gambar berdasarkan nilai yang diatur dengan slider.

Terima-Kasih
---
