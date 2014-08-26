#-------------------------------------------------------------------------------
# Name:         redcontour.py
# Purpose:      Captures real time video from webcam,filters the red color and a plot the largest contour
# Author:       @leopauly
# Created:     26-08-2014
#-------------------------------------------------------------------------------


import cv2
import numpy as np

vid=cv2.VideoCapture(0)  #give default value as  0
print vid.isOpened()  #Prints true if the camera is opened

i=0
while(vid.isOpened()):

    ret,image=vid.read()
    print ret # print true if the frame is captured properly
    img1=image
    blur=cv2.GaussianBlur(image,(5,5),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    lower=np.array([0,100,100])
    upper=np.array([6,255,255])
    mask=cv2.inRange(hsv,lower,upper)
    out=cv2.bitwise_and(image,image,mask=mask)

    gray = cv2.cvtColor(out,cv2.COLOR_BGR2GRAY)
    ret,thrs=cv2.threshold(gray,127,255,0)
    conts,h=cv2.findContours(thrs,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    big=0
    a=0
    n=len(conts)
    print n
    for i in range(1,n):
        if(len(conts[i])>a):
            big=i
            a=len(conts[i])

    cv2.drawContours(out,conts,big,(0,255,0),2)
    cv2.imshow('image',out)
    cv2.waitKey(100)

vid.release()
cv2.waitKey()
cv2.destroyAllWindows()








