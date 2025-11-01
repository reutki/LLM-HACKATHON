import cv2
import numpy as np

# Load the noisy QR code image
img = cv2.imread('images/distorted_qr.png', cv2.IMREAD_GRAYSCALE)

# 1. Median filter with larger kernel to remove more salt-and-pepper noise
median = cv2.medianBlur(img, 5)

# 2. Adaptive histogram equalization to correct radial gradient
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
equalized = clahe.apply(median)

# 3. Adaptive thresholding for binarization
thresh = cv2.adaptiveThreshold(equalized, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)

# 4. Morphological opening to remove small noise dots
kernel = np.ones((3, 3), np.uint8)
opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Save results
cv2.imwrite('images/denoised_qr.png', opened)

# Try to decode the QR code using OpenCV
detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(opened)
if data:
	print('Decoded QR code data:', data)
else:
	print('QR code could not be decoded. Trying more methods...')

	# Try Otsu's threshold
	_, otsu = cv2.threshold(equalized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	data2, _, _ = detector.detectAndDecode(otsu)
	if data2:
		print('Decoded with Otsu threshold:', data2)
	else:
		# Try inverting the image
		inv = cv2.bitwise_not(opened)
		data3, _, _ = detector.detectAndDecode(inv)
		if data3:
			print('Decoded with inverted image:', data3)
		else:
			# Try with a larger morphological kernel
			kernel5 = np.ones((5, 5), np.uint8)
			opened5 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel5)
			data4, _, _ = detector.detectAndDecode(opened5)
			if data4:
				print('Decoded with larger kernel:', data4)
			else:
				print('QR code could not be decoded by any method.')
print('Denoised image saved as images/denoised_qr.png')
