import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while True:
    # Take each frame
    ret, frame=cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    red=np.uint8([[[24,24,232]]])
    # define range of blue color in HSV
    low_blue= np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    redmask = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, low_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #cv2.imshow('frame', hsv)#display image
    #cv2.imshow('mask', mask)
    #cv2.imshow('res', res)
    cv2.imshow('redmask',redmask)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()