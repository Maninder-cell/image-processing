import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

im = cv2.imread('images/apple3.jpg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)

for data in set(label):
    print(f'Number of {data} in the image is '+ str(label.count(data)))
    
plt.imshow(output_image)
plt.show()



