import numpy as np
import cv2
cap = cv2.VideoCapture(0)

face_cascade_data= cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

while True:
    # Take each frame
    ret, frame=cap.read()
    # Convert BGR to HSV
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face_cascade_data.detectMultiScale(gray_frame,scaleFactor=1.1, minNeighbors=5)
    i=0
    for(x,y,w,h)in faces:
        print(x,y,w,h)
        roi_gray = gray_frame[y:y+h, x:x+w]#region of intereset for face coordinate and hight
        roi_color=frame[y:y+h,x:x+w]
        i=i+1
        img= f"Image{i}.png"
        cv2.imwrite(img,roi_gray)

        color =(255,0,0)# it is in bgr
        stroke=5
        end_cordinate_x = x + w
        end_cordinate_y = y + h
        cv2.rectangle(frame,(x,y),(end_cordinate_x, end_cordinate_y),color,stroke)
        print(x,y,w,h)


    cv2.imshow('frame', frame)#display image
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
