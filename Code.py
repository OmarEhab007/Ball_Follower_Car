import cv2
import numpy as np

cam = cv2.VideoCapture(0)

def empty():
    pass
cv2.namedWindow('mask')
cv2.createTrackbar('b','mask',0,255,empty)
cv2.createTrackbar('g','mask',0,255,empty)
cv2.createTrackbar('r','mask',0,255,empty)
cv2.createTrackbar('B','mask',0,255,empty)
cv2.createTrackbar('G','mask',0,255,empty)
cv2.createTrackbar('R','mask',0,255,empty)




while True:
    _,frame = cam.read()

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    b = cv2.getTrackbarPos('b','mask')
    g = cv2.getTrackbarPos('g','mask')
    r = cv2.getTrackbarPos('r','mask')
    B = cv2.getTrackbarPos('B','mask')
    G = cv2.getTrackbarPos('G','mask')
    R = cv2.getTrackbarPos('R','mask')
    lower = np.array([b,g,r])
    ubber = np.array([B,G,R])
    mask = cv2.inRange(hsv,lower,ubber)
    Contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for Contour in Contours:
        if cv2.contourArea(Contour)>1000:
            #cv2.drawContours(frame,Contour,-1,(0,255,0),3)
            x,y,w,h = cv2.boundingRect(Contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('mask',mask)
    cv2.imshow('frame',frame)

    k =  cv2.waitKey(5)
    if k == 27:
        break
cam.release()
cv2.destroyAllWindows()
    
    
