import func_dc

ffmpegpath = 'C:\ffmpeg-2023-06-08-git-024c30aa3b-full_build\bin'
video_name = 'input.mp4'
func_dc.scale_fps(18, video_name, ffmpegpath)
func_dc.slice_to_frames('output.mp4')
