"""

Note:
    - steering wheel should be light red
    - user should be 60cm far from the system
    - User should be in a place where there is a white background

"""

import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import pyautogui
import time


# initialize the video
cap = cv2.VideoCapture(0)

# color finder
myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 165, 'smin': 25, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}

# Variables
# posList = []


while True:
    success, img = cap.read()
    # img = cv2.imread("Resources/steering2.jpg")
    img = cv2.resize(img, (900, 700))
    img = cv2.flip(img, 1)

    # Find the steering
    imgColor, mask = myColorFinder.update(img, hsvVals)
    imgContours, contours = cvzone.findContours(img, mask, minArea=4500)
    hT, wT, cT = imgContours.shape

    # Drawing the rectangle                   H
    cv2.rectangle(imgContours, (0, 0), (270, 420), (0, 0, 255), 2)
    cv2.putText(imgContours, "LEFT", (170, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.rectangle(imgContours, (610, 0), (wT, 420), (0, 0, 255), 2)
    cv2.putText(imgContours, "RIGHT", (650, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    # cv2.rectangle(imgContours, (0, 270), (wT, 370), (0, 0, 255), 2)
    # cv2.putText(imgContours, "GO", (0, 300), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.rectangle(imgContours, (0, 420), (wT, hT), (0, 0, 255), 2)
    cv2.putText(imgContours, "STOP", (420, 500), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    cv2.putText(imgContours, "GO", (420, 40), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    if contours:
        cx, cy = contours[0]['center']
        print(cx, cy)
        cv2.circle(imgContours, (cx, cy), 10, (0, 255, 255), cv2.FILLED)
        if cy > 420:
            print("Car Is STOPPING.")
            pyautogui.press('down')
            # time.sleep(1)

        elif cx < 270:
            if cy < 420:
                print('Car Is Going LEFT.')
                pyautogui.press('left')
                # time.sleep(1)

        elif cx > 610:
            if cy < 420:
                print('Car Is Going RIGHT')
                pyautogui.press('right')
                # time.sleep(1)

        elif 270 < cx < 610:
            print('Car is MOVING')
            pyautogui.press('up')
            # time.sleep(1)

    # Display
    imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)
    # cv2.imshow('Images', img)
    cv2.imshow('imageColor', imgContours)
    cv2.waitKey(1)




# I will take my camera to repair
# I will make new steering wheel and update the code
# I will take my system to charge
# I will repair my bluetooth board
# I Will repair basketball prediction to work in a real life
# invisible cloak in a way that it will be updating the background image when ever the camera shake or every 5 sec

















# best:     {'hmin': 165, 'smin': 25, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}


# # import cv2
# # import cvzone
# # import numpy as np
# # from cvzone.ColorModule import ColorFinder
# #
# # # initialize the video
# # cap = cv2.VideoCapture(0)
# #
# # # color finder
# # myColorFinder = ColorFinder(False)
# # hsvVals = {'hmin': 165, 'smin': 25, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}
# #
# # # Variables
# # # posList = []
# #
# #
# # while True:
# #     success, img = cap.read()
# #     # img = cv2.imread("Resources/steering2.jpg")
# #     img = cv2.resize(img, (900, 700))
# #
# #     # Find the steering
# #     imgColor, mask = myColorFinder.update(img, hsvVals)
# #     imgContours, contours = cvzone.findContours(img, mask, minArea=4500)
# #
# #     if contours:
# #         cx, cy = contours[0]['center']
# #         print(cx, cy)
# #         cv2.circle(imgContours, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
# #
# #     # Display
# #     imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)
# #     # cv2.imshow('Images', img)
# #     cv2.imshow('imageColor', imgContours)
# #     cv2.waitKey(1)
#
# # best:     {'hmin': 165, 'smin': 25, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}
#
#
# # import cv2
# # import cvzone
# # import numpy as np
# # from cvzone.ColorModule import ColorFinder
# #
# # # initialize the video
# # cap = cv2.VideoCapture(0)
# #
# # # color finder
# # myColorFinder = ColorFinder(False)
# # hsvVals = {'hmin': 165, 'smin': 25, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}
# #
# # while True:
# #     success, img = cap.read()
# #     # img = cv2.imread("Resources/steering2.jpg")
# #     img = cv2.resize(img, (900, 700))
# #
# #     # Find the steering
# #     imgColor, mask = myColorFinder.update(img, hsvVals)
# #     # imContours, contours = cvzone.findContours(img, mask, minArea=3000)
# #
# #     # Display
# #     imgColor = cv2.resize(mask, (0, 0), None, 0.7, 0.7)
# #     # cv2.imshow('Images', img)
# #     cv2.imshow('imageColor', imgColor)
# #     cv2.waitKey(1)
# #
# # # best:     {'hmin': 165, 'smin': 25, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}
#
#
# import cv2
# import cvzone
# import numpy as np
# from cvzone.ColorModule import ColorFinder
#
# # initialize the video
# cap = cv2.VideoCapture(0)
#
# # color finder
# myColorFinder = ColorFinder(False)
# hsvVals = {'hmin': 165, 'smin': 25, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}
#
# # Variables
# # posList = []
#
#
# while True:
#     success, img = cap.read()
#     # img = cv2.imread("Resources/steering2.jpg")
#     img = cv2.resize(img, (900, 700))
#
#     # Find the steering
#     imgColor, mask = myColorFinder.update(img, hsvVals)
#     imgContours, contours = cvzone.findContours(img, mask, minArea=4500)
#
#     if contours:
#         cx, cy = contours[0]['center']
#         print(cx, cy)
#         cv2.circle(imgContours, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
#
#     # Display
#     imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)
#     # cv2.imshow('Images', img)
#     cv2.imshow('imageColor', imgContours)
#     cv2.waitKey(1)
#
# # best:     {'hmin': 165, 'smin': 25, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}
#
#
# # import cv2
# # import cvzone
# # import numpy as np
# # from cvzone.ColorModule import ColorFinder
# #
# # # initialize the video
# # cap = cv2.VideoCapture(0)
# #
# # # color finder
# # myColorFinder = ColorFinder(False)
# # hsvVals = {'hmin': 165, 'smin': 25, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}
# #
# # while True:
# #     success, img = cap.read()
# #     # img = cv2.imread("Resources/steering2.jpg")
# #     img = cv2.resize(img, (900, 700))
# #
# #     # Find the steering
# #     imgColor, mask = myColorFinder.update(img, hsvVals)
# #     # imContours, contours = cvzone.findContours(img, mask, minArea=3000)
# #
# #     # Display
# #     imgColor = cv2.resize(mask, (0, 0), None, 0.7, 0.7)
# #     # cv2.imshow('Images', img)
# #     cv2.imshow('imageColor', imgColor)
# #     cv2.waitKey(1)
# #
# # # best:     {'hmin': 165, 'smin': 25, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}
