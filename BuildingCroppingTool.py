import cv2
import numpy as np
flag = False
ix = -1
iy = -1

def draw(event,x,y,flags,params):
    global flag,ix,iy
    if event == 1:
        flag = True
        ix = x
        iy = y
    
    elif event == 0:
        if flag == True:
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=-1)


    elif event == 4:
        fx = x
        fy = y
        flag = False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=1)
        #Crop Tools
        cropped = img[iy:fy,ix:fx]
        cv2.imshow("New_Window",cropped)
        cv2.waitKey(0)
cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)
img = cv2.imread(r"C:\Users\vthak\OneDrive\Desktop\Image Processing Using OpenCV\img\2.png")
while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()    