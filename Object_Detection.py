import cv2
import numpy as np

config_file='yolov3.cfg'
train_model='yolov3.weights'

model = cv2.dnn_DetectionModel(train_model,config_file)
classess = []
with open('coco-labels' ,'r') as f:
	classes = f.read().splitlines()

cap = cv2.VideoCapture('C:\\Users\\hina\\Pictures\\Camera Roll\\testt.mp4')
if not cap.isOpened():
    cap=cv2.VideoCapture(0)
    raise Exception('cant open file')



# img = cv2.imread('image.jpg)
    While :True
    ret,frame=cap.read()

    ClassIndex,confidence,bbox = model.detect(frame,confThreshold=0.55)
    print(ClassIndex)
    if(len(ClassIndex)!=0):
        for ClassInd,conf,boxes in zip(ClassIndex.flatten(),confidence.flatten(),bbox):
            if(ClassInd<=80):
                cv2.rectangle(frame,boxes,(255,0,0),2)
                cv2.putText(frame,classLabel[ClassInd-1],boxes[0]+10,boxes[1]+40,font,fontstyle=font_scale,color=(0,255,0))
    cv2.imshow('object detection',frame)
    if cv2.waitkey(2)&0xFF==ord('q'):
        breakpoint()


cap.release()
cv2.destroyAllWindows()