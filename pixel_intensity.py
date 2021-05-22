import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('images/apple2.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HLS_FULL)

cv2.imshow('result',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()