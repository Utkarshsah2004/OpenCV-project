
#change width and height of the video
'''
import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 120)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,120)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while(cap.isOpened()): 
    ret, frame = cap.read()  

    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()  '''



import cv2
import datetime
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width: '+ str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+' Height: '+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        date_time = str(datetime.datetime.now())
        frame = cv2.putText(frame, text , (10,50), font,1,(0,255,255),2,cv2.LINE_AA)
        frame = cv2.putText(frame, date_time , (10,90), font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()












