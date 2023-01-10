import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Resources/cascades/data/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/nunez.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result", img)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break