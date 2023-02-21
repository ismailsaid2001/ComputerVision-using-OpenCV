import cv2
import numpy as np
img=cv2.imread('Ressources/Messi.jpg',0)
#laplacian filter (second order filter)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
#****************first order derivative filters************
#sobel filter
sobel_X=cv2.Sobel(img,cv2.CV_64F,1,0)
sobel_Y=cv2.Sobel(img,cv2.CV_64F,0,1)
sobel_X=np.uint8(np.absolute(sobel_X))
sobel_Y=np.uint8(np.absolute(sobel_Y))
#combine the 2 sobels
combine_sobelX_and_Y =cv2.bitwise_or(sobel_X,sobel_Y)
#Canny Edge Detection
#1st step :convert image to grayscale
#2nd step :applying a gaussian blur filter to the image for noise reduction
#3rd step :use sobel x and sobel y to get the edges in two directions
#4th:non maximum suppression (to make the edge thinner
#5 :thresholding : in this step we precise the min value and the max value
#each candidate whose intensity gradient  is above the max value is considered a confirmed edge ,candidates with intensity gradient below the min value
#are automatically eliminated and those in the interval [min,max] are accepted only if they are linked with a confirmed edge
img1= cv2.GaussianBlur(img,(5,5),0)
canny= cv2.Canny(img,100,200)
canny1= cv2.Canny(img1,100,200)
cv2.imshow('img',img)
# cv2.imshow('sobel_X',sobel_X)
# cv2.imshow('sobel_y',sobel_Y)
# cv2.imshow('laplacian',lap)
cv2.imshow('combined',combine_sobelX_and_Y)
cv2.imshow('canny',canny)
cv2.imshow('canny1',canny1)
#the blured image
cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()