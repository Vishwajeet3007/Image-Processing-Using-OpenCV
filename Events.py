import cv2
import numpy as np
def draw(event,x,y,flags,params):
    if event == 0:
        print("Mouse moved")
    elif event == 1:
        print("Mouse clicked")
    elif event == 4:
        print("Mouse up")
cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)
img = np.zeros((512,512,3))
while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()    