import cv2

class Frame:
    def __init__(self):
        self.frame = None
        self.name = ""
        self.check = None

    def applyGaussianBlurOnSelf(self):
        self.frame = cv2.GaussianBlur(self.frame, (21, 21), 0)

    def createGrayCopy(self):
        new_frame = Frame()
        new_frame.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        return new_frame

    def gaussianBlurGrayFrameCopy(self):
        self.frame = cv2.GaussianBlur(self.frame, (21, 21), 0)
        return cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

    def getFrame(self):
        return self.frame

    @staticmethod
    def applyAbsdiff(frameA, frameB):
        return cv2.absdiff(frameA.frame, frameB.frame)

    @staticmethod
    def applyThreshold(frameA):
        return cv2.threshold(frameA.frame, 22, 255, cv2.THRESH_BINARY)[1]

    @staticmethod
    def applyDilate(frameA, iterations):
        return cv2.dilate(frameA.frame, None, iterations=iterations)

    @staticmethod
    def findContours(frameA):
        return cv2.findContours(frameA.frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)