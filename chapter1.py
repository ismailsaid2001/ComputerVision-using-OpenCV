import cv2
#reading  image
# img=cv2.imread('Ressources/passat-18-tsi_used_0.jpeg')
# cv2.imshow("output",img)
# #in order to have some delay we use the function waitkey
# cv2.waitKey(1000)
# #displaying a video
#using the pc camera
cap=cv2.VideoCapture(0)
#using a saved video from ressources
# cap=cv2.VideoCapture("Ressources/video.mp4")
#width (id=3)
cap.set(3,640)
#height (id=4)
cap.set(4,480)
#brightness (id=10)
cap.set(10,100)
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1)&0xFF ==ord('q'):
        break
