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

cv2.waitKey(0)
cv2.destroyAllWindows()
