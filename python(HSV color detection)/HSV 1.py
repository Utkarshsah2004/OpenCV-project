import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,nothing) #creating a trckbar for Lower Hue
cv2.createTrackbar("LS","Tracking",0,255,nothing) #creating a trckbar for Lower Saturation
cv2.createTrackbar("LV","Tracking",0,255,nothing) #creating a trckbar for Lower Value
cv2.createTrackbar("UH","Tracking",255,255,nothing) #creating a trckbar for Upper Hue
cv2.createTrackbar("US","Tracking",255,255,nothing) #creating a trckbar for Upper Saturation
cv2.createTrackbar("UV","Tracking",255,255,nothing) #creating a trckbar for Upper Value

while True:
    frame = cv2.imread('Sample input-1.jpg')

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #changes the color to hsv

    lh = cv2.getTrackbarPos("LH","Tracking")
    ls = cv2.getTrackbarPos("LS","Tracking")
    lv = cv2.getTrackbarPos("LV","Tracking")
    uh = cv2.getTrackbarPos("UH","Tracking")
    us = cv2.getTrackbarPos("US","Tracking")
    uv = cv2.getTrackbarPos("UV","Tracking")

    lb = np.array([lh,ls,lv]) #Defines lower bounds for the color filtering
    ub = np.array([uh,us,uv]) #Defines upper bounds for the color filtering

    mask = cv2.inRange(hsv,lb,ub) #Creates a binary mask based on the specified HSV range.
    res = cv2.bitwise_and(frame,frame,mask=mask) #Applies the mask to the original frame using bitwise AND to extract the colored regions.


    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    key = cv2.waitKey(1)
    if key == 27:
        break

    

