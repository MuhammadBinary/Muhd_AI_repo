import requests
import cv2
import numpy as np
import imutils


def DAndroid_Cam(url, width=900, height=800):
    """
        :param url:
        :param width:
        :param height:
        :return: img
        """
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width, height)

    return img
    # cv2.imshow('Android Cam', img)


cv2.destroyAllWindows()
