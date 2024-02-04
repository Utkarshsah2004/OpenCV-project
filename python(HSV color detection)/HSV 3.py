import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread('Sample input-2.jpg', 0)

# Binary Thresholding
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

# Binary Inverted Thresholding
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

# Truncated Thresholding
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# To Zero Thresholding
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# To Zero Inverted Thresholding
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Binary Thresholding", th1)
cv2.imshow("Binary Inverted Thresholding", th2)
cv2.imshow("Truncated Thresholding", th3)
cv2.imshow("To Zero Thresholding", th4)
cv2.imshow("To Zero Inverted Thresholding", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()

