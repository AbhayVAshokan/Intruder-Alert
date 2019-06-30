# Syntax of filter2D

import cv2
import matplotlib.pyplot as pyt
import numpy as np


# ---------------------------------------- #
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#
#     frame = cv2.flip(frame, 1)
#
#     cv2.imshow("Webcam", frame)
#
#     if cv2.waitKey(1) == 13:
#         break
#
# cv2.imwrite("Original.jpg", frame)
# cv2.imwrite("Intruder.jpg", frame)

# --------------------------------------- #

original = cv2.imread("Original.jpg")
# intruder = cv2.imread("Intruder.jpg")

blur_original = cv2.GaussianBlur(cv2.cvtColor(original, cv2.COLOR_BGR2GRAY), (5, 5), 0)
# blur_intruder = cv2.GaussianBlur(cv2.cvtColor(intruder, cv2.COLOR_BGR2GRAY), (5, 5), 0)

cv2.imwrite("blur_original.jpg", blur_original)
# cv2.imwrite("blur_intruder", blur_intruder

ret, thresh_original = cv2.threshold(blur_original, 127, 255, cv2.THRESH_BINARY)
# ret, thresh_intruder = cv2.threshold(blur_intruder, 127, 255, cv2.THRESH_BINARY)

cv2.imwrite("thresh_original.jpg", thresh_original)
# cv2.imwrite("thresh_intruder.jpg", thresh_intruder)

# difference = np.absolute(thresh_original - thresh_intruder)
# cv2.imwrite("Difference.jpg", difference)

# kernel = np.array([1/6400 for i in range(original.shape[0])] for j in range(original.shape[1]))
# average = cv2.filter2D(difference, kernel, -1)
# cv2.imwrite("Average", average)

# --------------------------------------- #
