'''
#create a track bar

import numpy as np 
import cv2 as cv 


img = np.zeros((300,512,3),np.uint8)
cv.namedWindow('image') #created a named window with name image
def nothing(x):
    print(x)

cv.createTrackbar('B','image',0,255,nothing)  #nothing is a callback function and 0-255 is the range
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)


while(1) :
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')

    img[:] = [b, g, r]

cv.destroyAllWindows()  '''

'''
#on/off switch
import numpy as np 
import cv2 as cv 


img = np.zeros((300,512,3),np.uint8)
cv.namedWindow('image') #created a named window with n
def nothing(x):
    print(x)

cv.createTrackbar('B','image',0,255,nothing)  #nothing
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)


switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch,'image',0,1,nothing)


while(1) :
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    s = cv.getTrackbarPos(switch,'image')

    if s== 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows() '''


