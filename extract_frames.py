import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

vidcap = cv2.VideoCapture('Sidney_Coleman_lecture_01.mp4')
success,image = vidcap.read()
count = 0
while success:
    cv2.imwrite("data/frame%07i.png" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    count += 1
    if count > 10000:
        success = False