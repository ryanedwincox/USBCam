import cv2
import cv
import numpy as np
import time
cam1 = cv2.VideoCapture(0)
# cam2 = cv2.VideoCapture(3)
cam1.set(3, 480)
cam1.set(4, 640)
# cam2.set(3, 480)
# cam2.set(4, 640)
blank_image = np.zeros((480,640,3), np.uint8)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
while True:
    ret1, image1 = cam1.read()
    # print "image1: " + str(image1)
    # ret2, image2 = cam2.read()

    # hsvimg1 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(hsvimg1, lower_blue, upper_blue)
    # contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # maxArea = 0
    # for cnt in contours:
    #     area = cv2.contourArea(cnt)
    #     if area > maxArea:
    #         maxArea = area
    #         bestCnt = cnt

    # M = cv2.moments(bestCnt)
    # cx, cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    # cv2.circle(image1, (cx, cy), 5, [0, 0, 255], -1)

    x_offset = 0
    y_offset = 0
    blank_image[y_offset:y_offset+image1.shape[0], x_offset:x_offset+image1.shape[1]] = image1
    # x_offset = image1.shape[1]
    # blank_image[y_offset:y_offset+image2.shape[0], x_offset:x_offset+image2.shape[1]] = image2

    cv2.imshow('Camera', blank_image)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
    # time.sleep(0.1)

cam1.release()
# cam2.release()
cv2.destroyAllWindows()