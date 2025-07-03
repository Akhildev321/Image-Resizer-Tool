# 🖼️ Image Resizer Tool

A simple yet powerful Python tool that batch-resizes and converts images to PNG format using the **Pillow** library.

---

## 🚀 Features

- Resize multiple images in one go
- Convert all image formats to `.png`
- Save resized images into a new folder
- Clean terminal feedback for every image processed

---

## 🧰 Tech Stack

- Python 
- Pillow (PIL)
- OS Module

---

## ⚙️ How It Works

1. Reads all `.jpg`, `.jpeg`, `.png` images from the `input_images/` folder.
2. Resizes them to **300x300 pixels** using `Image.Resampling.LANCZOS`.
3. Converts them to `.png` format.
4. Saves them in the `resized_images/` folder.

---

**ChatGPT Screenshots in Screenshot Folder**
## 💡 What I Learned with the help of ChatGPT

- Python's `os` module for file and folder automation
- Image resizing with the Pillow (`PIL`) library
- Replacing deprecated `Image.ANTIALIAS` with `Image.Resampling.LANCZOS`
- Writing readable and reusable code
