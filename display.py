import cv2


class Display:

    def __init__(self):
        self.frame = []

    def displayAllFrames(self):
        for frame in self.frame:
            cv2.imshow("Frame: {}".format(frame.name), frame.frame)
        self.frame.clear()

    @staticmethod
    def closeAllWindows():
        cv2.destroyAllWindows()

