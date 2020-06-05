import numpy as np
import cv2 # python library (Open Computer Vision)


face_cascade = cv2.CascadeClassifier('C:/Users/Manvendra Mishra/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
#eye_cascade = cv2.CascadeClassifier('./haarcascade_lefteye_2splits.xml')
cap = cv2.VideoCapture(0)

while(True):
    ret, frame= cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
   # eye = eye_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) 
    for (x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
    """for (a,b,c,d) in eye:
        #print(x,y,w,h)
        roi_gray = gray[b:b+d, a:a+c]
        roi_color = frame[b:b+d, a:a+c]
        cv2.rectangle(frame, (a,b),(a+c,b+d),(255,0,0),2)"""
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27: 
        break 
               # wait for ESC key to exit
cv2.destroyAllWindows()







