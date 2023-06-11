import os
import cv2
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
from tqdm.notebook import tqdm
import subprocess
import ffmpeg


# check if an input file exists in the video input directory and return the path
def does_input_exists():
    files = []
    for i in glob.glob(r'video input/*'):
        files.append(i)
    return files


# convert video input to .mp4 file
def convert_to_mp4(path):
    subprocess.run(['ffmpeg', '-i', path, '-qscale', '0', 'input.mp4'])
    print('Video converted to an .mp4 file!')


# checks the framerate of the input video
def check_framerate(video):
    pass


# scales the framerate of the video
def scale_framerate(video, in_fps, out_fps):
    pass


# converts the video to frames
def convert_to_frames(video):
    vidcap = cv2.VideoCapture('video input/test.mp4')
    success, image = vidcap.read()
    count = 0
    success = True
    while success:
        success, image = vidcap.read()
        cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
        if cv2.waitKey(10) == 27:  # exit if Escape is hit
            break
        count += 1


# display input video
def show_input_vid(path):
    ipd.Video(path, width=800)
