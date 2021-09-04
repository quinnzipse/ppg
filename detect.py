import numpy as np
import cv2 as cv
import time

if __name__ == '__main__':
    face_cascade = cv.CascadeClassifier('frontal_face.xml')
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Camera won't open!")
        exit()

    detected_duration = 0
    detected_at = (0,0,0,0)
    detected_at_threshold = 7

    while True:
        successful, frame = capture.read()

        if not successful:
            print("Error recieving frame")
            break

        # processing
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = (), ()
        threshold = 10
        while len(faces) > 1:
            faces = face_cascade.detectMultiScale(gray, 1.3, threshold)
            threshold += 1

        for (x,y,w,h) in faces:
            cv.rectangle(gray, (x,y), (x+w,y+h), (255,255,0),2)
            same_face = abs(detected_at[0] - x) < detected_at_threshold and abs(detected_at[1] - y) < detected_at_threshold
            if same_face:
                detected_duration += 1
            else:
                detected_duration = 0
            
            detected_at = (x,y,w,h)
            center_x = int(x + (w / 2))
            center_y = int(y + (h / 2))
            radius = int( (w+h) /4)
        
            cv.circle(gray, (center_x, center_y), radius, (50 - detected_duration,detected_duration - 50,0),2)
        
        cv.imshow('detect_faces', gray)
        print(detected_duration)

        if cv.waitKey(30) == ord('q'):
            break
        
    cv.destroyAllWindows()
    capture.release()
