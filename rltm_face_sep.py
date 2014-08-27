#-------------------------------------------------------------------------------
# Name:        Real time face seperator
# Purpose:     Seperately displays the faces in a webcam stream in real time
# Author:      @leopauly
# Created:     27-08-2014
#-------------------------------------------------------------------------------

import cv2
import numpy as np

vid=cv2.VideoCapture(0)  #give default value as  0
print vid.isOpened()  #Prints true if the camera is opened
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


i=0
while(vid.isOpened()):

    ret,image=vid.read()
    print ret # print true if the frame is captured properly
    img1=image

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print faces
    i=1
    for (x,y,w,h) in faces:
     roi=img1 [y:y+h,x:x+w]
     j=str(i)
     cv2.imshow('face'+j,roi)
     cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
     i=i+1


    cv2.imshow('image',image)
    cv2.waitKey(100)

vid.release()
cv2.waitKey()
cv2.destroyAllWindows()








