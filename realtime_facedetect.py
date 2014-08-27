# By : @leopauly
# Purpose : Detect the faces in the given webcam video stream in real time using a pretrained haar classifier
# created on : 27-8-2014

import cv2
import numpy as np

vid=cv2.VideoCapture(0)  #give default value as  0
print vid.isOpened()  #Prints true if the camera is opened 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #give the exact path for the xml file


i=0
while(vid.isOpened()):

    ret,image=vid.read()
    print ret # print true if the frame is captured properly
    img1=image

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  #returns the x,y(center) & w,h(length and breadth of enclsosing rect)
    print faces
    for (x,y,w,h) in faces:
     img = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)


    cv2.imshow('image',image)
    cv2.waitKey(100)

vid.release()
cv2.waitKey()
cv2.destroyAllWindows()








