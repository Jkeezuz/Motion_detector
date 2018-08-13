import cv2


class Camera:

    def __init__(self, camera_number):
        self.camera_number = camera_number
        self.video = None

    def startRecording(self):
        self.video = cv2.VideoCapture(self.camera_number)
        return self.video

    def getVideo(self):
        return self.video

    def getFrame(self):
        return self.video.read()

    def realeaseVideo(self):
        if self.video is not None:
            self.video.release()
        else:
            return False



