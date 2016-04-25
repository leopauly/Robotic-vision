# Program for real time edge detection using canny edge detector.
# writtern by : @leopauly | meetleopauly@yahoo.com

import cv2
import time 
import math
import numpy as np

vidobj=cv2.VideoCapture(0) #initialises a video objet named vidobj


while True:
    
    ret,image=vidobj.read() # captures video from the webcamera each from at a time
    #cv2.imshow('stream',image) # displays the captured frame from webcamera
    
    th=100  #threshold for canny edge detector
    h,w,d=image.shape
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # converts the rgb frame to grey image
    blur = cv2.medianBlur (grey,15) # uses a median blur to filter out the image
    edgeim=cv2.Canny(blur, th / 2, th)
    edgeim2=cv2.Canny(grey, th / 2, th)
    
    print h,w,d
    grid = np.zeros([h, 3*w, 3], np.uint8)
    grid[0:h, 0:w] = image                        # grid 1 : orginal rgb image
    grid[0:h, w:w*2] = np.dstack([edgeim] * 3)    # grid 2 : edge detection done on the image blured using median filter
    grid[0:h, w*2:w*3] = np.dstack([edgeim2] * 3) # grid 2 : edge detection done on the orginal image
    cv2.imshow('edgedetection',grid) 
    
    if cv2.waitKey(1) & 0xFF ==ord ('q'):
       break
