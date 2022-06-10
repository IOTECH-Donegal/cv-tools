""""
DisplayWebcam
Screen display from camera 0 to RawImages directory
Tested with Python >=3.9

By: JOR
    v0.1    10JUN22     First draft

"""
# Reference: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html


import os
import cv2
import numpy as np

# Reference
# https://docs.opencv.org/4.x/

print('Utility to capture video from the WebCam and store in RawVideos directory')
input('Press ENTER to continue...')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
