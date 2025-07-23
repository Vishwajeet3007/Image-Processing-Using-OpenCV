import cv2
import numpy as np

# read an image
img = cv2.imread(r"C:\Users\vthak\OneDrive\Desktop\Image Processing Using OpenCV\img\2.png")
print(type(img))
print(img.shape)

# Converting into grayscale
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Displayed Image", img_gray)

# Playing with RGB color

# img[:,:,1] = 0
# imgBlue = img[:,:,0]
# imgGreen = img[:,:,1]
# imgRed = img[:,:,2]
# new_img = np.hstack((imgBlue,imgGreen,imgRed))

# cv2.imshow("Displayed Image", new_img)

# # # Resize
# img_resize = cv2.resize(img,(256,256))
# cv2.imshow("Displayed Image",img_resize)

# # Flipping an Image
# img_flip = cv2.flip(img,-1)
# cv2.imshow("Displayed Image",img_flip)

# # Croping an image
# img_crop = img[:300,:300]
# cv2.imshow("Displayed Image",img_crop)

# # Saving an image
# cv2.imwrite("fruits.png",img_crop)

# Drawing shapes and Text on Image(Rectangle ,Circle,Line,Text)
cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)
cv2.circle(img,center=(100,150),radius=100,color=(0,0,255),thickness=3)
cv2.line(img,pt1=(0,0),pt2=(512,512),thickness=2,color=(0,255,0))
cv2.putText(img,org=(100,100),fontScale=4,fontFace=cv2.FONT_ITALIC,color=(0,255,255),thickness=2,lineType=cv2.LINE_AA,text='Car')
# Events

cv2.imshow("Displayed Image",img)
cv2.waitKey(0)       # Wait for a key press
cv2.destroyAllWindows()  # Close the window
