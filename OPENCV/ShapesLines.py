import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)

#print(img)
#img[200:300,100:300] = 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(100,10),(200,300),(120,104,123),2)
cv2.circle(img,(200,200),25,(102,234,255),cv2.FILLED)
cv2.putText(img,"Haryana Aale",(250,100),cv2.FONT_ITALIC,1,(245,213,102),4)

cv2.imshow("Image",img)

print(img.shape)

cv2.waitKey(0)