# max(), minMaxLoc(), traverse matrix, jump through 100 method

import cv2
import numpy as np


# Function to return the next frame from the webCam in grayscale.
cap = cv2.VideoCapture(0)
def nextFrame():
    ret, webCam_frame = cap.read()
    frame = np.flip(webCam_frame, 1)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    ret, thresh_frame = cv2.threshold(blur_frame, 127, 255, cv2.THRESH_BINARY)
    return frame, thresh_frame



# Function to check whether there is an intruder.
def checkIntruder(current_frame, next_frame):
    output = np.absolute(current_frame - prev_frame)
    M = [[1/6400 for i in range(80)] for j in range(80)]
    kernel = np.array(M)
    average = cv2.filter2D(output, -1, kernel)
    cv2.imshow("Average", average)
    return average.max() >= 150



# Start of the main function.
ret, prev_frame = nextFrame()
frames = []

while True:
    frame, current_frame = nextFrame()
    frames.append(current_frame)

    cv2.imshow("WebCam Output", frame)
    cv2.imshow("Image Difference", np.absolute(current_frame - prev_frame))

    if(checkIntruder(current_frame, prev_frame)):
        cv2.imshow("Intruder", frame)
        cv2.imwrite("Intruder.jpg", frame)
        break

    if len(frames) == 10:
        prev_frame = frames[0]
        del(frames[0])

    if cv2.waitKey(1) == 13:
        break

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
