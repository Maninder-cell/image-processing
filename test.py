import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('images/apple2.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)

weaker = np.array([0,0,100])
stronger = np.array([10,255,255])

#Threshold hsv image to obtain input color
mask = cv2.inRange(hsv, weaker, stronger) 

#colour segmentation
res = cv2.bitwise_and(image,image, mask= mask)

result = image.copy()
contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
x = 0
for cntr in contours:
    x,y,w,h = cv2.boundingRect(cntr)
    cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 2)
    print("x,y,w,h:",x,y,w,h)
    x+=1
print(x)


#Show original image , mask and result
cv2.imshow('mask',mask)  
cv2.imshow('Result',result)  

cv2.waitKey(0)
cv2.destroyAllWindows()

