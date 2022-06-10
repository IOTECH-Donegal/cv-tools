""""
ImageProcessor
Browse images in RawImages directory, do processing and then save in ProcessedImages directory
Tested with Python >=3.9

By: JOR
    v0.1    10JUN22     First draft

"""
# Reference: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html


import os
import cv2
import numpy as np

print('Utility to browse images stored in RawImages directory')
print('With the ability to save individual frames to ProcessedImages directory')
print('Press n to go to the next window and s to save, q to quit')
input('Press ENTER to continue...')

# CV uses image variable as a numpy array
current_image = np.array([])
filename = ""

# Find the current path of the Python scripts
current_path = os.getcwd()

# It is assummed the raw images are in a subdirectory
raw_images_directory = (os.path.join(os.getcwd(), "RawImages"))
processed_images_directory = (os.path.join(os.getcwd(), "ProcessedImages"))

def read_image(fullpath, incolor):
    # Use the global numpy array, current_image
    global current_image
    current_image = cv2.imread(fullpath, incolor)

def write_image(fullpath):
    # Use the global numpy array, current_image
    global current_image, filename
    cv2.imwrite(fullpath, current_image)

def show_image():
    # Use the global numpy array, current_image
    global current_image, filename
    # Use filename as the title of the window
    cv2.imshow(filename, current_image)
    

# Main programme
if __name__ == "__main__":
    for filename in os.listdir(raw_images_directory):
        # Create the full path to the image
        readpath = os.path.join(os.getcwd(), "RawImages", filename)
        # Load the image into the image_image global, when reading, set -1 = Untouched, 1 = Color, 0 = B&W
        read_image(readpath, 1)
        # Display the image which was read in
        show_image()
        # Either move on by hitting "d" or save by hitting "s"
        key_press = cv2.waitKey()
        if key_press == ord('q'):
            break
        elif key_press == ord('n'):
            cv2.destroyAllWindows
        elif key_press == ord('s'):
            # Test write an image back
            writepath = os.path.join(os.getcwd(), "ProcessedImages", filename)
            write_image(writepath)
            cv2.destroyAllWindows
