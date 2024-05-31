import cv2
import cvzone
import pyttsx3
import random


'''
  Filters:
        beard,
        cool,
        native,
        pirate,
        star,
        sunglass
'''
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread('images/cool.png', cv2.IMREAD_UNCHANGED)

while True:
    save = random.randint(2, 800)
    save2 = random.randint(2, 700)
    success, frame = cap.read()
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(imgGray)
    for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])


    cv2.imshow('SnapChat', frame)
    if cv2.waitKey(10) & 0XFF == ord('s'):
        cv2.imwrite(f'{save}.jpg', frame)
