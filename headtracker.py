#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SAMSUNG
#
# Created:     27-08-2014
# Copyright:   (c) SAMSUNG 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cv2
import numpy as np

vid=cv2.VideoCapture(0)  #give default value as  0
print vid.isOpened()  #Prints true if the camera is opened
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


i=0
a=210
b=190
while(vid.isOpened()):

    ret,image=vid.read()
    print ret # print true if the frame is captured properly
    img1=image

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print faces
    for (x,y,w,h) in faces:
     c1=a-x   #Change in position of head in x coordinate
     c2=b-y   #Change in position of head in y coordinate
     print c1,c2  #The change in head position w.r.t to a central point is printed
     img = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)


    cv2.imshow('image',image)
    cv2.waitKey(100)

vid.release()
cv2.waitKey()
cv2.destroyAllWindows()








