import cv2
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

combine_audio(video_name, audio_name, 'test.mp4')

# image_folder = 'data'
# video_name = 'video.avi'

# images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
# print(images)
# frame = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, layers = frame.shape

# video = cv2.VideoWriter(video_name, 0, 30, (width,height))

# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))

# cv2.destroyAllWindows()
# video.release()


# https://stackoverflow.com/a/61063349/5238625

# def combine_audio(vidname, audname, outname, fps=25):
#     import moviepy.editor as mpe
#     my_clip = mpe.VideoFileClip(vidname)
#     audio_background = mpe.AudioFileClip(audname)
#     final_clip = my_clip.set_audio(audio_background)
#     final_clip.write_videofile(outname,fps=fps)

####################
# import os
# import sys
# from moviepy.editor import VideoFileClip


# def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
#     """Converts video to audio using MoviePy library
#     that uses `ffmpeg` under the hood"""
#     filename, ext = os.path.splitext(video_file)
#     clip = VideoFileClip(video_file)
#     clip.audio.write_audiofile(f"{filename}.{output_ext}")


# if __name__ == "__main__":
#     vf = sys.argv[1]
#     convert_video_to_audio_moviepy(vf)

# vidcap = cv2.VideoCapture('Sidney_Coleman_lecture_01.mp4')
# success,image = vidcap.read()
# count = 0
# while success:
#     cv2.imwrite("data/frame%d.jpg" % count, image)     # save frame as JPEG file      
#     success,image = vidcap.read()
#     count += 1
#     if count > 1000:
#         success = False
  # img_arr = np.array(image)
  # print(img_arr.shape)
  # plt.imshow(image)
  # plt.show()


# from torchvision import models as model
# import torch
# dir(model)
# alexnet = model.alexnet(pretrained=True)
# print(alexnet)