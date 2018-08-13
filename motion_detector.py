import datetime

import cv2, time
import pandas as pandas

video = cv2.VideoCapture(1)

frame_counter = 0


first_frame = None

status_list = [None, None]

times = []

df = pandas.DataFrame(columns=["Start", "End"])

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    frame_counter = frame_counter + 1
    check, frame = video.read()
    is_there_motion = False
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame)
    thresh_frame = cv2.threshold(delta_frame, 22, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=3)

    (_,cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour=contour) < 1000:
            continue
        is_there_motion = True
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 120, 34), 3)

    status_list.append(is_there_motion)
    if status_list[-1] is True and status_list[-2] is False:
        times.append(datetime.datetime.now())
    if status_list[-1] is False and status_list[-2] is True:
        times.append(datetime.datetime.now())
    cv2.imshow("Gray", gray_frame)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Threshold", thresh_frame)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if is_there_motion is True:
            times.append(datetime.datetime.now())
        break

print(times)

for i in range(0, len(times), 2):
    df=df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()

cv2.destroyAllWindows()