
# Track the Thief - Video Processing and OCR

## Overview
This project processes surveillance or challenge videos to extract the movement trail of objects (such as cars or people) and attempts to recognize any visible letters or numbers using Optical Character Recognition (OCR). The code uses OpenCV for video processing and background subtraction, and Tesseract (via pytesseract) for OCR.

For each video in the input folder, the script:
- Tracks moving objects and accumulates their paths.
- Outputs a binary image showing the movement trail.
- Runs OCR on the resulting image to guess any visible characters.
- Saves the output images and prints OCR results.

## Setup Guidelines

### 1. Install Python dependencies
You need Python 3.7+ and the following packages:

```
pip install opencv-python numpy
```

### 2. Prepare your video files
Place your video files (e.g., `.mp4`, `.avi`) in the folder specified by `INPUT_FOLDER` in `main.py` (default: `/Users/dcambur/Public/hackathon/videos/track_the_thief/`).

### 4. Run the script
From the project directory, run:

```
python main.py
```

Output images and OCR results will be saved in the `out_letters` folder.

---
**Note:** You can adjust parameters such as frame skip, downscale factor, and minimum contour area in the configuration section of `main.py`.
