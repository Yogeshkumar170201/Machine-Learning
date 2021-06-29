import cv2
import numpy as np

img = cv2.imread("Resources/Aadhar.jpg")

height,width=580,844
pts1 = np.float32([[433,325],[1277,325],[433,905],[1277,905]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)