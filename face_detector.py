import cv2, time

video = cv2.VideoCapture(1)

frame_counter = 0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    frame_counter = frame_counter + 1
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3)

    for x, y, width, height in faces:
        img = cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 3)

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()

cv2.destroyAllWindows()