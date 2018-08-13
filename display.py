import cv2


class Display:

    def __init__(self):
        self.first_frame = None
        self.gray_frame = None
        self.current_frame = None
        self.delta_frame = None
        self.thresh_frame = None

    def displayAllFrames(self):
        cv2.imshow("Gray", self.gray_frame)
        cv2.imshow("Delta", self.delta_frame)
        cv2.imshow("Threshold", self.thresh_frame)
        cv2.imshow("Frame", self.current_frame)

    @staticmethod
    def closeAllWindows():
        cv2.destroyAllWindows()

