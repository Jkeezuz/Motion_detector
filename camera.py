import cv2

from frame import Frame


class Camera:

    def __init__(self, camera_number):
        self.camera_number = camera_number
        self.video = None

    def startRecording(self):
        self.video = cv2.VideoCapture(self.camera_number)
        return self.video

    def getVideo(self):
        return self.video

    def getFrameObject(self):
        new_frame = Frame()
        new_frame.check, new_frame.frame = self.video.read()
        return new_frame

    def realeaseVideo(self):
        if self.video is not None:
            self.video.release()
        else:
            return False



