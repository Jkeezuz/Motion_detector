import datetime

import cv2
import pandas as pandas
from camera import Camera
from graph_maker import GraphMaker
from motiondetector import MotionDetector
from display import Display


motion_detector = MotionDetector()
camera = Camera(1)
motion_detector.attachCamera(camera)
motion_detector.startCamera()
display = Display()
motion_detector.attachDisplay(display)
df = pandas.DataFrame(columns=["Start", "End"])

motion_detector.startDetecting()

print(motion_detector.times)

for i in range(0, len(motion_detector.times), 2):
    df=df.append({"Start": motion_detector.times[i], "End": motion_detector.times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")


p = GraphMaker.generateQuadGraphDatetime(df)


motion_detector.getCamera().realeaseVideo()

display.closeAllWindows()