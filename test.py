import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('images/apple1.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)

weaker = np.array([0,0,100])
stronger = np.array([10,255,255])

#Threshold hsv image to obtain input color
mask = cv2.inRange(hsv, weaker, stronger) 

#colour segmentation
res = cv2.bitwise_and(image,image, mask= mask)

#Show original image , mask and result
cv2.imshow('Image',image)
cv2.imshow('mask',mask)  
cv2.imshow('Result',res)  

cv2.waitKey(0)
cv2.destroyAllWindows()

