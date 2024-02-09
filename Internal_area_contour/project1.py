import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy

img = cv2.imread('7.jpeg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img1=copy.deepcopy(img)

# Global Thresholding
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Adaptive Thresholding
#th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Display the images
cv2.imshow("Global Thresholding", th1)
#cv2.imshow("Adaptive Thresholding", th2)

kernal=np.ones((2,2),np.uint8)
dilation = cv2.dilate(th1,kernal)
#cv2.imshow('dilated',dilation)



contour,hierarchy = cv2.findContours(th1,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
biggest_contour = max(contour,key = cv2.contourArea)

cv2.drawContours(img,biggest_contour,-1,(0,255,0),4)
cv2.imshow('dilated',dilation)
cv2.imshow('img',img)


for contour in contour:
    # Compute the area of the contour
    area = cv2.contourArea(contour)
    print("Internal area of contour:", area)

print("Number of contours:", len(contour))




#cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
