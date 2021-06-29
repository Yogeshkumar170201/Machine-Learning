import cv2
import numpy as np

img = cv2.imread("Resources/PARA.jpg")
print(img.shape)

imgResize = cv2.resize(img,(1000,500))

imgCropped =  img[100:200,0:50]

cv2.imshow("Image",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)
print(imgResize.shape)

cv2.waitKey(0)