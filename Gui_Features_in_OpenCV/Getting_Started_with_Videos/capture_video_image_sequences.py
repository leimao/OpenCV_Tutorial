import cv2

# save frequency for video frames
SAVE_FREQUENCY = 100

# start index
INDEX_START = 0

# end index
INDEX_END = 5000

# image file extension
IMAGE_EXTENSION = '.jpg'

cap = cv2.VideoCapture('sample_video/sample_video.mp4')

# convert the whole video file to a sequence of image files
index = 0
img_num = 0
while (cap.isOpened()):
    # ret = False: video end / capture failure
    ret, frame = cap.read()
    if (ret == False) or (index > INDEX_END):
        break

    if (index >= INDEX_START) and (index <= INDEX_END) and (index % SAVE_FREQUENCY == 0):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        filename = 'captured_video_image_sequences/' + 'img_' + '{0:08d}'.format(img_num) + IMAGE_EXTENSION
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, 30])
        img_num += 1

        print(filename + ' saved')

    index += 1

cap.release()
cv2.destroyAllWindows()


