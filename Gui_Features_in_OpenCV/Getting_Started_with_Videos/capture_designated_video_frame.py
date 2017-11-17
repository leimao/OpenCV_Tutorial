import cv2

# image file extension
IMAGE_EXTENSION = '.jpg'

# designate video frame number
INDEX_DESIGNATED = 200

# Read certain frame from the video

'''
# Python: cv2.VideoCapture.set(propId, value) → retval
https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html
propId –

Property identifier. It can be one of the following:
CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
CV_CAP_PROP_FPS Frame rate.
CV_CAP_PROP_FOURCC 4-character code of codec.
CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
CV_CAP_PROP_HUE Hue of the image (only for cameras).
CV_CAP_PROP_GAIN Gain of the image (only for cameras).
CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
CV_CAP_PROP_WHITE_BALANCE_U The U value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_WHITE_BALANCE_V The V value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_ISO_SPEED The ISO speed of the camera (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_BUFFERSIZE Amount of frames stored in internal buffer memory (note: only supported by DC1394 v 2.x backend currently)

value – Value of the property.
'''

cap = cv2.VideoCapture('sample_video/sample_video_2.mp4')
cap.set(cv2.CAP_PROP_POS_FRAMES, INDEX_DESIGNATED)
ret, frame = cap.read()
filename = 'captured_designated_image_frames/' + 'video_frame_' + str(INDEX_DESIGNATED) + IMAGE_EXTENSION
cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, 30])
print(filename + ' saved')
cap.release()
