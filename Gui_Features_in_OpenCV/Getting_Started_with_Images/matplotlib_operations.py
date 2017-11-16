import cv2
import matplotlib.pyplot as plt

img = cv2.imread("jordan.jpg", cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # Hide tick labels
plt.show()