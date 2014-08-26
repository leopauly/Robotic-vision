#-------------------------------------------------------------------------------
# Name:         red
# Purpose:      Displays red coloured objects only in real time from the video captured from the webcam
# Author:       @leopauly
# Created:     26-08-2014
#-------------------------------------------------------------------------------


import cv2
import numpy as np

vid=cv2.VideoCapture(0)  #give default value as  0
print vid.isOpened()  #Prints true if the camera is opened

i=0
while(vid.isOpened()): #remains inside the loop as long as the vid object keeps the webcam opened
    ret,image=vid.read()
    print ret # print true if the frame is captured properly
    blur=cv2.GaussianBlur(image,(5,5),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lower=np.array([0,100,100])
    upper=np.array([6,255,255])
    mask=cv2.inRange(hsv,lower,upper)
    out=cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow('image',out)
    i=i+1
    cv2.waitKey(100)

vid.release()
cv2.waitKey()
cv2.destroyAllWindows()







