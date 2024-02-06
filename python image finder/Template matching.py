import cv2
import numpy as np



img = cv2.imread("Sample input-1(1).jpg")
flag=0
def shape():
    flag=0
    try:

        template = cv2.imread("s2.jpg")

        w, h = template.shape[::2] #for drawing shape on the matched image

        res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)

        print(res)

        hold = 0.9
        loc = np.where(res >= hold)
        print(loc)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h), (0,0,255),2) #draw the rectangle
            
        flag=1
        cv2.imshow("img",img)


    except :
        '''img = cv2.imread('Sample input-1.jpg', 0)
        
        # Global Thresholding
        _, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        # Adaptive Thresholding
        #th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

        # Display the images
        cv2.imshow("Global Thresholding", th1)
        #cv2.imshow("Adaptive Thresholding", th2)'''

        print("Thank you")
        breakpoint

    if flag == 0:
        try:

            template = cv2.imread("s1.jpg")

            w, h = template.shape[::2] #for drawing shape on the matched image

            res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)

            print(res)

            hold = 0.9
            loc = np.where(res >= hold)
            print(loc)

            for pt in zip(*loc[::-1]):
                cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h), (0,0,255),2) #draw the rectangle
                
            flag=1
            cv2.imshow("img",img)


        except :
            print("Thank you 2")
            breakpoint

        
        

shape()

'''
template = cv2.imread("s1.jpg")

w, h = template.shape[::2] #for drawing shape on the matched image

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)

print(res)

hold = 0.9
loc = np.where(res >= hold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h), (0,0,255),2) #draw the rectangle
            

cv2.imshow("img",img) '''


cv2.waitKey(0)
cv2.destroyAllWindows()