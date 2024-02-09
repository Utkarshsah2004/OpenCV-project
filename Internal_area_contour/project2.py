import cv2

img = cv2.imread('1.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Global Thresholding
_, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(th1, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Draw contours on the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 4)

# Display the image with contours
cv2.imshow("Image with Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Calculate and print area of each contour
for contour in contours:
    area = cv2.contourArea(contour)
    print("Internal area of contour:", area)

print("Number of contours:", len(contours))

# Conditional processing based on contour area
for contour in contours:
    area = cv2.contourArea(contour)
    print("Internal area of contour:", area)
    if area >= 1500:
        _, th3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
        cv2.imshow("Truncated Thresholding", th3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        break
