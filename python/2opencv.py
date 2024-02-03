'''import cv2

cap = cv2.VideoCapture(0);

while(True):
    ret, frame = cap.read()  #capture frame from camera
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  #ord() is used for pressing the keys
        break

cap.release()
cv2.destroyAllWindows '''

'''
#for gray image
import cv2

cap = cv2.VideoCapture(0);

while(True):
    ret, frame = cap.read()  #capture frame from camera

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #CHANGES BGR TO GRAY VIDEO

    cv2.imshow('frame',gray) #gray video
    if cv2.waitKey(1) & 0xFF == ord('q'):  #ord() is used for pressing the keys
        break

cap.release()
cv2.destroyAllWindows'''


'''
#Uses of functions

import cv2

cap = cv2.VideoCapture(0);

while(cap.isOpened()):  #isOpened fn is used for true checking . if true then only it will get proceed 
    ret, frame = cap.read()  

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #It prints the frame width 
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  #It prints the frame height

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows  '''



#For saving webcam videos "FOURCC"

import cv2

cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4',fourcc,20.0, (640,480))  #cv2.VideoWriter(Name of the output file.extention of the file,fourcc,no. of frames per sec,size)

while(True):
    ret, frame = cap.read()  # 'ret' is a boolean variable. It checks the frame, if the frame is true then proceed otherwise false
    if ret == True:

        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  #ord() is used for pressing the keys
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows














