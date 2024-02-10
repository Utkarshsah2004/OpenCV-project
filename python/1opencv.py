import cv2

img = cv2.imread('j.jpg',-1)

print(img)

cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('jj.png',img)
    cv2.destroyAllWindows()
