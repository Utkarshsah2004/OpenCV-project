import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Sample input-1', 0)  # Read in grayscale
_, threshold = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(threshold, kernel, iterations=1)
erosion = cv2.erode(threshold, kernel, iterations=1)
gradient = cv2.morphologyEx(threshold, cv2.MORPH_GRADIENT, kernel)

plt.subplot(3, 2, 1)
plt.imshow(img, cmap='gray')  # Specify cmap for grayscale image
plt.title('Original Image')

plt.subplot(3, 2, 2)
plt.imshow(threshold, cmap='gray')
plt.title('Threshold')

plt.subplot(3, 2, 3)
plt.imshow(erosion, cmap='gray')
plt.title('Erosion')

plt.subplot(3, 2, 4)
plt.imshow(dilation, cmap='gray')
plt.title('Dilation')

plt.subplot(3, 2, 5)
plt.imshow(gradient, cmap='gray')
plt.title('Gradient')

plt.tight_layout()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

