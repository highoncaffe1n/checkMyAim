import func
import IPython.display as ipd

#func.show_input_vid('test.mp4')
#ipd.Video('test.mp4', width=700)

cap = func.cv2.VideoCapture('video input/test.mp4')
print(cap.get(func.cv2.CAP_PROP_FRAME_COUNT))
capture = func.cv2.VideoCapture()
