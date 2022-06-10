""""
RecordWebcam
Recordings are made from camera 0 to RawImages directory
Tested with Python >=3.9

By: JOR
    v0.1    10JUN22     First draft

"""
# Reference: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

import numpy as np
import cv2 
import os, sys

from file_utilities import log_file_name

print('Utility to record webcam videos, save in the RawVideos directory')
input('Press ENTER to continue...')

# It is assummed the raw videos are in a subdirectory
raw_videos_directory = (os.path.join(os.getcwd(), "RawVideos"))
filename = (os.path.join(os.getcwd(), "RawVideos", log_file_name(".avi")))

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object, FourCC is a 4-byte code used to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# Set the output
fps = 20.0
height = 640
width = 480
out = cv2.VideoWriter(filename, fourcc, fps, (height,  width))

while cap.isOpened():
    # Get the frame and a return value
    ret, frame = cap.read()
    # If return value = 0, no video stream 
    if not ret:
        print("No video stream.")
        break
    # write the frame
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()