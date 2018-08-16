import cv2


class Display:

    def __init__(self):
        self.frame = []

    def displayAllFrames(self):
        for frame in self.frame:
            cv2.imshow("Frame: {}".format(frame.name), frame.frame)


    @staticmethod
    def closeAllWindows():
        cv2.destroyAllWindows()

    def clearFrames(self):
        self.frame.clear()

