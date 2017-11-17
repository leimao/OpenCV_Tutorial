import cv2

# Read unchanged jpeg image
img1 = cv2.imread('jordan.jpg', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('jordan.png', cv2.IMREAD_UNCHANGED)

'''
For JPEG, it can be a quality ( CV_IMWRITE_JPEG_QUALITY ) from 0 to 100 (the higher is the better). Default value is 95.
For WEBP, it can be a quality ( CV_IMWRITE_WEBP_QUALITY ) from 1 to 100 (the higher is the better). By default (without any parameter) and for quality above 100 the lossless compression is used.
For PNG, it can be the compression level ( CV_IMWRITE_PNG_COMPRESSION ) from 0 to 9. A higher value means a smaller size and longer compression time. Default value is 3.
For PPM, PGM, or PBM, it can be a binary format flag ( CV_IMWRITE_PXM_BINARY ), 0 or 1. Default value is 1.
'''

# save compressed jpeg image
cv2.imwrite('jordan_compressed.jpg', img1, [cv2.IMWRITE_JPEG_QUALITY, 30])
# save compressed jpeg image
# compression effect not significant
cv2.imwrite('jordan_compressed.png', img1, [cv2.IMWRITE_PNG_COMPRESSION, 9])



