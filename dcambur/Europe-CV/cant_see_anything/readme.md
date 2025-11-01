# QR Code Denoising and Decoding

## Overview
This project demonstrates how to denoise a heavily distorted QR code image and attempt to decode it using OpenCV. The pipeline includes median filtering, adaptive histogram equalization, adaptive thresholding, morphological operations, and multiple decoding strategies to maximize the chance of successful QR code reading.

## How it Works
- Loads a noisy QR code image from `images/distorted_qr.png`.
- Applies median filtering to reduce salt-and-pepper noise.
- Uses CLAHE (adaptive histogram equalization) to correct for radial gradient/vignetting.
- Applies adaptive thresholding and morphological opening to further clean the image.
- Attempts to decode the QR code using OpenCV's `QRCodeDetector`.
- If the initial attempt fails, tries Otsu's threshold, image inversion, and a larger morphological kernel.
- Saves the denoised image as `images/denoised_qr.png` and prints the decoded data if successful.

## Setup & Usage

### 1. Install Dependencies
You need Python 3 and the following packages:

```
pip install opencv-python numpy
```

### 2. Place the Input Image
Put your noisy QR code image as `images/distorted_qr.png` in the project directory.

### 3. Run the Script
From the `cant_see_anything` folder, run:

```
python main.py
```

### 4. Output
- The denoised image will be saved as `images/denoised_qr.png`.
- The script will print the decoded QR code data if successful, or report failure after trying several methods.

---
**Tip:**
If the QR code is still not readable, try adjusting the median filter size, morphological kernel, or thresholding parameters in `main.py`.
