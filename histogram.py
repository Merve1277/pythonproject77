import cv2
import numpy as np

Hist=[0 for i in range(256)]
I=cv2.imread("tavsan7_1.jpg",0)
cv2.imshow("merve77",I)
cv2.waitKey(0)
print(I.shape)
w, h = I.shape[:2]
for v in range (0,h):
    for u in range (0,w):
        i = I[u,v]
        Hist[i]=Hist[i]+1
print(Hist)