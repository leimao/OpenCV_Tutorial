# import numpy
import cv2

'''
Read and Show Images
cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. 
It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
'''
img = cv2.imread("jordan.jpg", cv2.IMREAD_COLOR)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Show Images in Pre-created Window

By default, the flag is cv2.WINDOW_AUTOSIZE. 
But if you specify flag to be cv2.WINDOW_NORMAL, you can resize window.
'''

cv2.namedWindow('img', cv2.WINDOW_NORMAL) # You can change the window size
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Write Image
'''

cv2.imwrite('jordan.png', img)
# print('\"jodan.png\" saved.')