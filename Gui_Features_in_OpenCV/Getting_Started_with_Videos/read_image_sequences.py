import cv2

# read a sequence of images
# image file name has to start from img_00000000 and has increament of 1 without missing values in the middle

cap = cv2.VideoCapture('captured_video_image_sequences/img_%08d.jpg')

index = 0
while (cap.isOpened()):
    # ret = False: video end / capture failure
    ret, frame = cap.read()
    if (ret == False):
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    index += 1

cap.release()
cv2.destroyAllWindows()

