import cv2
import datetime

from Motion_detector.frame import Frame


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

    def getFrameObject(self):
        return self.camera.getFrameObject()

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

    def drawRectsOnMotion(self, cnts, current_frame):
        for contour in cnts:
            if cv2.contourArea(contour=contour) < 1000:
                continue
            self.MotionInFrame()
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(current_frame, (x, y), (x + w, y + h), (255, 120, 34), 3)

    def recordMotionTime(self):
        self.status_list.append(self.is_there_motion)
        if self.status_list[-1] is True and self.status_list[-2] is False:
            self.times.append(datetime.datetime.now())
        if self.status_list[-1] is False and self.status_list[-2] is True:
            self.times.append(datetime.datetime.now())

    def waitForKeyPress(self, time, pkey):
        key = cv2.waitKey(time)
        if key == ord(pkey):
            if self.getMotionStatus() is True:
                self.times.append(datetime.datetime.now())
            return True
        return False

    def startDetecting(self):
        first_frame = Frame()
        delta_frame = Frame()
        thresh_frame = Frame()
        delta_frame.name = "Delta"
        thresh_frame.name = "Thresh"


        while True:
            current_frame = self.getFrameObject()
            self.noMotionInFrame()
            current_frame.name = "Current"

            gray_frame = current_frame.createGrayCopy()
            gray_frame.applyGaussianBlurOnSelf()
            gray_frame.name = "Gray"
            if first_frame.frame is None:
                first_frame.frame = gray_frame.frame
                continue

            delta_frame.frame = Frame.applyAbsdiff(first_frame, gray_frame)
            thresh_frame.frame = Frame.applyThreshold(delta_frame)
            thresh_frame.frame = Frame.applyDilate(thresh_frame, 3)

            (_, cnts, _) = Frame.findContours(thresh_frame)

            self.drawRectsOnMotion(cnts, current_frame.frame)

            self.recordMotionTime()


            self.display.frame.append(delta_frame)
            self.display.frame.append(thresh_frame)
            self.display.frame.append(current_frame)
            self.display.frame.append(gray_frame)

            self.display.displayAllFrames()

            if self.waitForKeyPress(1, 'q') is True:
                break