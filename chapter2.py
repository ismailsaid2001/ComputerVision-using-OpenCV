import cv2
img=cv2.imread("ressources/passat-18-tsi_used_0.jpeg")
#converting an image to grayscale
#pay attention : in opencv we use the BGR convention instead of RGB
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#applying blur to the image
imgBlur= cv2.GaussianBlur(imgGray,(7,7),0)
#edge detection
imgCanny= cv2.Canny(img,150,200)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.waitKey(0)