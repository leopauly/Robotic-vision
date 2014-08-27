
#-------------------------------------------------------------------------------
# Name:        faceseperator
# Purpose:     seperately displays all the faces in the given image
# Author:      @leopauly
# Created:     27-08-2014
#-------------------------------------------------------------------------------

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image=cv2.imread('new.jpg',1)
img1=image
cv2.imshow('leo',image)


gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print faces
i=1
for (x,y,w,h) in faces:
 roi=img1 [y:y+h,x:x+w]  #seperates each face from orginal image
 j=str(i)
 cv2.imshow('face'+j,roi)  #displays each face
 cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
 i=i+1

cv2.imshow('image',image) #displays orginal image with all faces marked
cv2.waitKey(100)


cv2.waitKey(00)
cv2.destroyAllWindows()

