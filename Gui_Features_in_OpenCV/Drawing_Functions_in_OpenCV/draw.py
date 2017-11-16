import numpy as np 
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0,0), (511,511), (255,0,0), 5)

# Draw a rectangle
img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

# Draw a circle
img = cv2.circle(img, (447,63), 63, (0,0,255), -1) # -1 for infinite thickness

# Draw  a ellipse
img = cv2.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)

# Add text to image

'''
To put texts in images, you need specify following things.
Text data that you want to write
Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
Font type (Check cv2.putText() docs for supported fonts)
Font Scale (specifies the size of font)
regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended.
'''
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 2, cv2.LINE_AA)


# Save image
cv2.imwrite('opencv.png', img)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()