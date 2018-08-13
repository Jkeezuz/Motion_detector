import cv2
import datetime

class MotionDetector:

    def __init__(self):
        self.camera = None
        self.is_there_motion = False
        self.status_list = [None, None]
        self.times = []
        self.display = None

    def attachCamera(self, camera):
        self.camera = camera

    def attachDisplay(self, display):
        self.display = display

    def startCamera(self):
        self.camera.startRecording()

    def getFrame(self):
        return self.camera.getFrame()

    def getCamera(self):
        return self.camera

    def noMotionInFrame(self):
        self.is_there_motion = False

    def MotionInFrame(self):
        self.is_there_motion = True

    def getMotionStatus(self):
        return self.is_there_motion

    def createGrayFrame(self):
        self.display.gray_frame =  cv2.cvtColor(self.display.current_frame, cv2.COLOR_BGR2GRAY)

    def applyGaussianBlur(self):
        self.display.gray_frame = cv2.GaussianBlur(self.display.gray_frame, (21, 21), 0)

    def startDetecting(self):
        while True:
            check, self.display.current_frame = self.getFrame()
            self.noMotionInFrame()
            self.createGrayFrame()
            self.applyGaussianBlur()

            if self.display.first_frame is None:
                self.display.first_frame = self.display.gray_frame
                continue

            self.display.delta_frame = cv2.absdiff(self.display.first_frame, self.display.gray_frame)
            self.display.thresh_frame = cv2.threshold(self.display.delta_frame, 22, 255, cv2.THRESH_BINARY)[1]
            self.display.thresh_frame = cv2.dilate(self.display.thresh_frame, None, iterations=3)

            (_, cnts, _) = cv2.findContours(self.display.thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in cnts:
                if cv2.contourArea(contour=contour) < 1000:
                    continue
                self.MotionInFrame()
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(self.display.current_frame, (x, y), (x + w, y + h), (255, 120, 34), 3)

            self.status_list.append(self.is_there_motion)
            if self.status_list[-1] is True and self.status_list[-2] is False:
                self.times.append(datetime.datetime.now())
            if self.status_list[-1] is False and self.status_list[-2] is True:
                self.times.append(datetime.datetime.now())

            self.display.displayAllFrames()

            key = cv2.waitKey(1)

            if key == ord('q'):
                if self.getMotionStatus() is True:
                    self.times.append(datetime.datetime.now())
                break