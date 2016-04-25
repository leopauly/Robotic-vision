# Program real time circle detection
#written by : @leopauly | meetleopauly@yahoo.com

import cv2
import numpy as np
import cv2.cv as cv
capture = cv2.VideoCapture(0)

while True:    
    ret,img=capture.read()
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(grey, 15)
    
    t=100 
    sc = 1
    md = 30
    at = 40
    circles = cv2.HoughCircles(blur, cv.CV_HOUGH_GRADIENT, sc, md, t, at)   # circle detection
    if circles is not None:
        x, y, radius = int(circles[0][0][0]), int(circles[0][0][1]), int(circles[0][0][2])
        print(x, y, radius)                               # prints the center and the radius of the circle
        cv2.circle(img, (x, y), radius, (0, 0, 255), 1)   # draws the circle on the orignal image 
        cv2.circle(img, (x, y), 1, (0, 0, 255), 1)        # marks the center of the drawn circle
        
    cv2.imshow('Image with detected circle', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
