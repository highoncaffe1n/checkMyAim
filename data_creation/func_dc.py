import ffmpeg
import sys
import cv2


def scale_fps(fps, path, ffmpegpath):
    sys.path.append(r''+ ffmpegpath)
    stream = ffmpeg.input(path)
    stream = stream.filter('fps', fps=fps, round='up').filter('scale')
    stream = ffmpeg.output(stream, 'output.mp4')
    ffmpeg.run(stream)
    return print('done!')


def slice_to_frames(path):
    vidcap = cv2.VideoCapture('output.mp4')
    success, image = vidcap.read()
    count = 0
    success = True
    while success:
        print(count)
        success, image = vidcap.read()
        cv2.imwrite("frames/frame%d.jpg" % count, image)  # save frame as JPEG file
        if cv2.waitKey(10) == 27:  # exit if Escape is hit
            break
        count += 1

