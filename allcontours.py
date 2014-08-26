#-------------------------------------------------------------------------------
# Purpose:    plots all the contours in the webcam stream in real time
# Author:     @leopauly
# Created:    26-08-2014
#-------------------------------------------------------------------------------


import cv2
import numpy as np

vid=cv2.VideoCapture(0)  #give default value as  0
print vid.isOpened()  #Prints true if the camera is opened

i=0
while(vid.isOpened()):

    ret,image=vid.read()
    print ret # print true if the frame is captured properly

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,thrs=cv2.threshold(gray,127,255,0)
    conts,h=cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(image,conts,-1,(0,255,0),2)
    cv2.imshow('image',image)
    cv2.waitKey(100)

vid.release()
cv2.waitKey()
cv2.destroyAllWindows()
