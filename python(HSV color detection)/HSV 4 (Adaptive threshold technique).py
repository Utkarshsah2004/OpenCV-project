import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread('Sample input-1.jpg', 0)

# Global Thresholding
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Adaptive Thresholding
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Display the images
cv2.imshow("Global Thresholding", th1)
cv2.imshow("Adaptive Thresholding", th2)

cv2.waitKey(0)
cv2.destroyAllWindows()
