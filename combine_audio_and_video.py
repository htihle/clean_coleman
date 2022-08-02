import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
# import moviepy.editor as mpe
from moviepy.editor import *

def combine_audio(vidname, audname, outname, fps=25):
    
    my_clip = VideoFileClip(vidname)
    audio_background = AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

  
video_name = 'movie.mp4' #'AST9240_Noise.mp4'
audio_name = 'test_zoom.mp4'
outname = 'test.mp4'

combine_audio(video_name, audio_name, outname)