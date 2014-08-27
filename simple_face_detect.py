#------------------------------------------------------------------------------
# Purpose:     detects the faces in the given image using pretrained haar clssifier
# Author:      @leopauly
# Created:     27-08-2014
#------------------------------------------------------------------------------


import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image=cv2.imread('leo.jpg',1)
cv2.imshow('leo',image)
img1=image

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print faces

for (x,y,w,h) in faces:
 img = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow('image',image)
cv2.waitKey(100)


cv2.waitKey(5000)
cv2.destroyAllWindows()



