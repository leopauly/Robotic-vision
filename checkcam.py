# Program to check if the camera feed is obatined properly
#written by : @leopauly | meetleopauly@yahoo.com

import cv2
import numpy as np

capture=cv2.VideoCapture(0)

while True:
    ret,image=capture.read()
    cv2.imshow('stream',image)  #displays the live stream from webcam
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    cv2.imshow('streamgrey',grey) #displays the live stream from webcam converted to greay scale
    cv2.imshow('streamrgb',np.dstack([grey]*3)) #displays the live stream from webcam converted back to rgb from greay scale
    
    if cv2.waitKey(1) & 0xFF ==ord ('q'):
       break
