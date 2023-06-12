from testing import func

#func.show_input_vid('input.mp4')
#ipd.Video('input.mp4', width=700)

cap = func.cv2.VideoCapture('video input/input.mp4')
print(cap.get(func.cv2.CAP_PROP_FRAME_COUNT))
capture = func.cv2.VideoCapture()
