import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

image_folder = 'data'
video_name = 'video.avi'

framerate = 29.920168

frame_files = os.listdir(image_folder)

images = [img for img in sorted(frame_files) if img.endswith(".png")]

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape


video = cv2.VideoWriter(video_name, 0, framerate, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()