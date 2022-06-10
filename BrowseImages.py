import os
import cv2
import numpy as np

print('Utility to browse videos stored in RawVideos directory')
print('With the ability to save individual frames to ProcessedImages directory')
input('Press ENTER to continue...')

# Global variables
filename = ""
current_video = np.array([])

# Find the current path of the Python scripts
current_path = os.getcwd()


# It is assummed the raw videos are in a subdirectory
raw_videos_directory = (os.path.join(os.getcwd(), "RawVideos"))
processed_videos_directory = (os.path.join(os.getcwd(), "ProcessedVideos"))

def read_video(video_source):
    # Use the global numpy array, current_video
    global current_video
    frame_counter = 0
    current_video = cv2.VideoCapture(video_source)
    while(current_video.isOpened()):
        ret, current_frame = current_video.read()
        cv2.imshow("Press n for next frame, s to save the frame, q to quit", current_frame)  
        # Key Handler
        key =  cv2.waitKey(0)
        while key not in [ord('q'), ord('n'), ord('s')]:
            key = cv2.waitKey(0)
        if key == ord('q'):
            break
        elif key == ord('n'):
            # Keep a count of the frame numbers
            frame_counter += 1
        elif key == ord('s'):
            # The filename will be the frame number .jpg
            filename = str(frame_counter) + ".jpg"
            # Get a full write path
            writepath = os.path.join(os.getcwd(), "ProcessedVideos", filename)
            # Then save the current frame
            cv2.imwrite(writepath, current_frame)


# Main programme
if __name__ == "__main__":
    # Test the webcam first
    #read_video(0)
    
    # Now iterate through video files
    for filename in os.listdir(raw_videos_directory):
        # Create the full path to the image
        readpath = os.path.join(os.getcwd(), "RawVideos", filename)
        # Load the image into the image_image global, when reading, set -1 = Untouched, 1 = Color, 0 = B&W
        #read_video(readpath)
        read_video(readpath)
