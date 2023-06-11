import os
import cv2
import glob


# check if an .mp4 file exists in the video input directory
def does_input_exists():
    files = []
    for i in glob.glob(r'video input/*.mp4'):
        files.append(i)
    return files


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
