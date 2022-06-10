import os
import cv2
import numpy as np

print('Utility to browse videos stored in RawVideos directory')
print('With the ability to extract all frames to ProcessedImages directory')
input('Press ENTER to continue...')

# Global variables
filename = ""
current_video = np.array([])

# Find the current path of the Python scripts
current_path = os.getcwd()

# It is assummed the raw videos are in a subdirectory
raw_videos_directory = (os.path.join(os.getcwd(), "RawVideos"))
processed_videos_directory = (os.path.join(os.getcwd(), "ProcessedVideos"))

def extract_images(video_source):
    # Use the global numpy array, current_video
    global current_video
    frame_counter = 0  
    
    current_video = cv2.VideoCapture(video_source)
    # How many frames per second
    fps = current_video.get(cv2.CAP_PROP_FPS)
    print(f"Frames per second: {fps}")

    number_of_frames = int(current_video.get(cv2. CAP_PROP_FRAME_COUNT))
    print(f"Total number of frames: {number_of_frames}")
    
    for frame_counter in range(number_of_frames):
        ret, current_frame = current_video.read()
        # The filename will be the frame number .jpg
        filename = str(frame_counter) + ".jpg"
        # Get a full write path
        writepath = os.path.join(os.getcwd(), "ProcessedVideos", filename)
        # Then save the current frame
        cv2.imwrite(writepath, current_frame)