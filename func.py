import os
import cv2

# checks the format of the input video
def check_format(video):
    os.listdir('/video input/')
    file_name, file_extension = os.path.splitext('/video input/' + str(video))
    return file_extension


# converts the video to a mp4 file
def convert_to_mp4(video, vid_format):
    pass


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
