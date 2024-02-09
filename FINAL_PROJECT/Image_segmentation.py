import cv2
import numpy as np
     
img = cv2.imread('1.jpeg') #Enter the image name
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convert the image to HSV
im1=hsv.copy()
im2=hsv.copy()
im3=hsv.copy()
def first():
    a = 0  # Initial lower hue threshold
    b = 0  # Initial lower saturation threshold
    while True:
        lb = np.array([0, 0, a])  # Define lower bounds for the color filtering
        ub = np.array([255, 255, 255])  # Define upper bounds for the color filtering
        mask = cv2.inRange(hsv, lb, ub)  # Create a binary mask based on the specified HSV range.

        # Calculate contours
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 1:  # Check if a single contour is found
            area = cv2.contourArea(contours[0])  # Calculate the area of the contour
            if 50 < area < 500:  # Check if the area is within the desired range
                cv2.imshow("mask", mask)
                cv2.waitKey(0)  # Wait indefinitely until a key is pressed
                break

        # Increment lower hue threshold
        a += 1

        if a >= 255:  # Exit loop if lower hue threshold exceeds maximum
            a = 0  # Reset lower hue threshold
            b = 0  # Reset lower saturation threshold
            while b < 255:
                c = 0  # Reset lower value threshold
                while c < 255:
                    lb = np.array([0, b, c])  # Define lower bounds for the color filtering
                    mask = cv2.inRange(hsv, lb, ub)  # Create a binary mask based on the specified HSV range.

                    # Calculate contours
                    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    if len(contours) == 1:  # Check if a single contour is found
                        area = cv2.contourArea(contours[0])  # Calculate the area of the contour
                        if 50 < area < 500:  # Check if the area is within the desired range
                            cv2.imshow("mask", mask)
                            cv2.waitKey(0)  # Wait indefinitely until a key is pressed
                            break
                    c += 1
                if len(contours) == 1:
                    break
                b += 1
            if len(contours) == 1:
                break
            else:
                a += 1  # Increment a if no suitable thresholds found for b and c


a = 0  # Initial lower hue threshold
while True:
    lb = np.array([a, 0, 0])  # Define lower bounds for the color filtering
    ub = np.array([255, 255, 255])  # Define upper bounds for the color filtering
    mask = cv2.inRange(im1, lb, ub)  # Create a binary mask based on the specified HSV range.

    # Calculate contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 1:  # Check if a single contour is found
        area = cv2.contourArea(contours[0])  # Calculate the area of the contour
        if 50 < area < 500 :  # Check if the area is within the desired range
            cv2.imshow("mask", mask)
            cv2.waitKey(0)  # Wait indefinitely until a key is pressed
            break

    # Increment lower hue threshold
    a += 1

    if a >= 255:  # Exit loop if lower hue threshold exceeds maximum
        break

# Call the first function
first()

        
a = 0  # Reset lower hue threshold
while a < 255:
    b = 0  # Reset lower saturation threshold
    while b < 255:
        lb = np.array([a, b, 0])  # Define lower bounds for the color filtering
        ub = np.array([255, 255, 255])
        mask = cv2.inRange(im2, lb, ub)  # Create a binary mask based on the specified HSV range.

        # Calculate contours
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 1:  # Check if a single contour is found
            area = cv2.contourArea(contours[0])  # Calculate the area of the contour
            if 50 < area < 500:  # Check if the area is within the desired range
                cv2.imshow("mask", mask)
                cv2.waitKey(0)  # Wait indefinitely until a key is pressed
                break
        b += 1
    if len(contours) == 1:
        break
    a += 1


e=255
while e > 0:
    f = 0  # Reset lower saturation threshold
    while b < 255:
        lb = np.array([0, 0, 0])  # Define lower bounds for the color filtering
        ub = np.array([e, f, 255])
        mask = cv2.inRange(im3, lb, ub)  # Create a binary mask based on the specified HSV range.

        # Calculate contours
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 1:  # Check if a single contour is found
            area = cv2.contourArea(contours[0])  # Calculate the area of the contour
            if 50 < area < 500:  # Check if the area is within the desired range
                cv2.imshow("mask", mask)
                cv2.waitKey(0)  # Wait indefinitely until a key is pressed
                break
        f-= 1
    if len(contours) == 1:
        break
    e-= 1


cv2.destroyAllWindows()
