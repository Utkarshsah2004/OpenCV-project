import cv2
import numpy as np

img = cv2.imread('1.jpeg')

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)  # creating a trackbar for Lower Hue
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)  # creating a trackbar for Lower Saturation
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)  # creating a trackbar for Lower Value
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)  # creating a trackbar for Upper Hue
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)  # creating a trackbar for Upper Saturation
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)  # creating a trackbar for Upper Value

while True:
    frame = img.copy()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # change the color to HSV

    lh = cv2.getTrackbarPos("LH", "Tracking")
    ls = cv2.getTrackbarPos("LS", "Tracking")
    lv = cv2.getTrackbarPos("LV", "Tracking")
    uh = cv2.getTrackbarPos("UH", "Tracking")
    us = cv2.getTrackbarPos("US", "Tracking")
    uv = cv2.getTrackbarPos("UV", "Tracking")

    lb = np.array([lh, ls, lv])  # Defines lower bounds for the color filtering
    ub = np.array([uh, us, uv])  # Defines upper bounds for the color filtering

    mask = cv2.inRange(hsv, lb, ub)  # Creates a binary mask based on the specified HSV range.
    res = cv2.bitwise_and(frame, frame, mask=mask)  # Applies the mask to the original frame using bitwise AND to extract the colored regions.

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to exit
        break

# Calculate contours outside the loop
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
cv2.imshow("Contours", frame)
print("Number of contours:", len(contours))

for cnt in contours:
    area = cv2.contourArea(cnt)
    print("Area of contour:", area)

cv2.destroyAllWindows()
