import ffmpeg

import sys

sys.path.append(r'C:\ffmpeg-2023-06-08-git-024c30aa3b-full_build\bin')

stream = ffmpeg.input('test.mp4')

stream = stream.filter('fps', fps=12, round='up').filter()

stream = ffmpeg.output(stream, 'output.mp4')
