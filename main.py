import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Fungsi untuk memuat gambar
def load_image():
    global img, img_display, img_original
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        img_original = img.copy()  # Simpan salinan gambar asli
        img_display = img.copy()  # Simpan salinan untuk ditampilkan
        display_image(img)

# Fungsi untuk menyimpan gambar
def save_image():
    if img_display is None:
        messagebox.showerror("Error", "No image to save!")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        cv2.imwrite(file_path, img_display)
        messagebox.showinfo("Image Saved", "Image saved successfully!")

# Fungsi untuk menampilkan gambar di GUI
def display_image(image):
    global img_display
    img_display = image
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(image=img_pil)
    panel.config(image=img_tk)
    panel.image = img_tk

# Fungsi untuk reset gambar ke kondisi sebelumnya
def reset_image():
    global img_display
    if img_original is None:
        messagebox.showerror("Error", "No image loaded!")
        return
    img_display = img_original.copy()
    display_image(img_display)

# Fungsi untuk peningkatan kontras
def enhance_contrast():
    global img_display
    if img is None:
        messagebox.showerror("Error", "No image loaded!")
        return
    img_yuv = cv2.cvtColor(img_display, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    img_contrast = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    display_image(img_contrast)

# Fungsi untuk peningkatan ketajaman
def enhance_sharpness():
    global img_display
    if img is None:
        messagebox.showerror("Error", "No image loaded!")
        return
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    img_sharp = cv2.filter2D(img_display, -1, kernel)
    display_image(img_sharp)

# Fungsi untuk reduksi noise
def reduce_noise():
    global img_display
    if img is None:
        messagebox.showerror("Error", "No image loaded!")
        return
    img_denoised = cv2.fastNlMeansDenoisingColored(img_display, None, 10, 10, 7, 21)
    display_image(img_denoised)

# Fungsi untuk penyesuaian kecerahan
def adjust_brightness(value):
    global img_display
    if img is None:
        messagebox.showerror("Error", "No image loaded!")
        return
    brightness = int(value)
    img_bright = cv2.convertScaleAbs(img_display, beta=brightness)
    display_image(img_bright)

# Inisialisasi Tkinter
root = Tk()
root.title("Image Enhancement Application")

# Frame untuk menampilkan gambar
panel = Label(root)
panel.pack(padx=10, pady=10)

# Tombol untuk load, save, reset, dan enhance
btn_frame = Frame(root)
btn_frame.pack(fill=X, padx=10, pady=10)

load_btn = Button(btn_frame, text="Load Image", command=load_image)
load_btn.pack(side=LEFT, padx=5)

save_btn = Button(btn_frame, text="Save Image", command=save_image)
save_btn.pack(side=LEFT, padx=5)

reset_btn = Button(btn_frame, text="Reset Image", command=reset_image)
reset_btn.pack(side=LEFT, padx=5)

contrast_btn = Button(btn_frame, text="Enhance Contrast", command=enhance_contrast)
contrast_btn.pack(side=LEFT, padx=5)

sharp_btn = Button(btn_frame, text="Enhance Sharpness", command=enhance_sharpness)
sharp_btn.pack(side=LEFT, padx=5)

denoise_btn = Button(btn_frame, text="Reduce Noise", command=reduce_noise)
denoise_btn.pack(side=LEFT, padx=5)

# Slider untuk penyesuaian kecerahan
brightness_label = Label(root, text="Adjust Brightness:")
brightness_label.pack()

brightness_slider = Scale(root, from_=-100, to=100, orient=HORIZONTAL, command=adjust_brightness)
brightness_slider.pack(fill=X, padx=10)

# Variabel global
img = None
img_display = None
img_original = None

# Jalankan aplikasi
root.mainloop()
