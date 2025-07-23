import cv2
import numpy as np
def draw(event,x,y,flags,params):

    if event == 1:
        cv2.circle(img,center=(x,y),radius=50,color=(0,0,255),thickness=-1)
    
cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)
img = cv2.imread(r"C:\Users\vthak\OneDrive\Desktop\Image Processing Using OpenCV\img\2.png")
while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()  