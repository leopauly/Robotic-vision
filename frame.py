#-------------------------------------------------------------------------------
# Name:         frame.py
# Purpose:      Captures a frame from your webcam and displays it
# Author:       @leopauly
# Created:      26-08-2014
#------------------------------------------------------------------------------


import cv2
import numpy as np

vid=cv2.VideoCapture(0)  #give default value as  0
print vid.isOpened()  #Prints true if the camera is opened

i=0
while(i<2):
    ret,image=vid.read()
    print ret # print true if the frame is captured properly
    cv2.imshow('image',image)
    i=i+1

vid.release()
cv2.waitKey()
cv2.destroyAllWindows()







