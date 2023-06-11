import func
import IPython.display as ipd
import cv2
#func.show_input_vid('test.mp4')
ipd.Video('test.mp4', width=700)

cap = cv2.VideoCapture('test.mp4')
print(cap.get(cv2.cv2.CAP_PROP_FRAE_COUNT))
capture = cv2.VideoCapture()
