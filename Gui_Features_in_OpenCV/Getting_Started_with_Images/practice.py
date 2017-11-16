# import numpy
import cv2

img = cv2.imread('jordan.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)


'''
Sometimes if key does not work, try:
If you are using a 64-bit machine, you will have to modify k = cv2.waitKey(0) line 
as follows : k = cv2.waitKey(0) & 0xFF
'''

k = cv2.waitKey(0)
if k == 27:  # Hit ESC
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('jordan_gray.png', img)
    cv2.destroyAllWindows()

