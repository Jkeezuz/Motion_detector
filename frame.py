import cv2

class Frame:
    def __init__(self):
        self.frame = None

    def applyGaussianBlur(self):
        self.frame = cv2.GaussianBlur(self.frame, (21, 21), 0)

    def createGrayCopy(self):
        return cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)