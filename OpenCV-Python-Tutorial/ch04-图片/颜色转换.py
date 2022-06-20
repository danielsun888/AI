# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 17:15
# @Author  : play4fun
# @File    : 颜色转换.py
# @Software: PyCharm

"""
颜色转换.py:
"""
import cv2
img = cv2.imread('messi5.jpg',cv2.IMREAD_UNCHANGED)#包括图像的 alpha 通道


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', gray)#窗口会自动调整为图像大小

temp = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)#灰色转RGB
cv2.imshow('temp', temp)#窗口会自动调整为图像大小
k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.destroyAllWindows()
