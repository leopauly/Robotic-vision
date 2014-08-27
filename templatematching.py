#-------------------------------------------------------------------------------
# Name:        templatematching
# Purpose:     Object Detection using template matching technoque
# Author:      @leopauly
# Created:     27-08-2014
#-------------------------------------------------------------------------------

import cv2
import numpy as np

s=cv2.imread('n.jpg',1)
t=cv2.imread('n1.jpg',1)
cv2.imshow('s',s)
cv2.imshow('t',t)
h,w,n= t.shape
print h,w


methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

method = eval(methods[0])  #change values 0,1,2,3,4,5 so as to use different tempelate matching techniques
print method
res = cv2.matchTemplate(s,t,method)
min,max,minloc,maxloc = cv2.minMaxLoc(res)
x,y=maxloc              #use minloc instead of maxloc for 'cv2.TM_SQDIFF' AND 'cv2.TM_SQDIFF_NORMED'
img = cv2.rectangle(s,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('new',s)


cv2.waitKey()
