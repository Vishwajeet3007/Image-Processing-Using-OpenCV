import cv2
import numpy as np
cap = cv2.VideoCapture(0)

# Defining the codec and create Videowriter object 
fourcc = cv2.VideoWriter_fourcc(*'xvid')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret , frame = cap.read()
    if not ret:
        break

    out.write(frame)

    cv2.imshow('webcam',frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()