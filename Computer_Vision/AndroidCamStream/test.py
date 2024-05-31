import cv2
import numpy as np
from ADcam import DAndroid_Cam

url = 'http://192.168.224.8:8080/shot.jpg'
while True:
    try:
        img = DAndroid_Cam(url, width=600, height=800)
    except:
        img = np.zeros_like(img)

    cv2.imshow('Android Stream', img)
    cv2.waitKey(1)


























# import cv2
# from ADcam import DAndroid_Cam
#
#
# url = 'http://192.168.21.158:8080/shot.jpg'
# while True:
#     img = DAndroid_Cam(url)
#     cv2.imshow('Android Stream', img)
#     cv2.waitKey(1)
