import cv2
import numpy as np
#first of all wwe create a black image
img1= np.zeros((250,500,3),dtype=np.uint8) #height:250,width:500
#creating a white rectangle
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
#here we create a white image
img2=np.full((250,500,3),255,dtype=np.uint8)
#applying a black rectangle on the img2
img2=cv2.rectangle(img2,(0,0),(250,250),(0,0,0),-1)
#bitwise operations :
#these perators will be applied pixel by pixel
bitAnd= cv2.bitwise_and(img2,img1)
bitXor= cv2.bitwise_xor(img2,img1)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow('And',bitAnd)
cv2.imshow('And',bitXor)
cv2.waitKey(0)
