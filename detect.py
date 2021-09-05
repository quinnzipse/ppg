import numpy as np
import cv2 as cv
import time
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas

fig = Figure()
canvas = FigureCanvas(fig)
axis = fig.subplots()
axis.set_title("Red Histogram")

avgs = list()
avgs.append(0)

upsndowns = ""
count = 0


def getRedHistogram(input_frame):
    blurred_img = cv.blur(input_frame, (3,3))
    # preprocessed = cv.convertScaleAbs(blurred_img, alpha=1.2, beta=0)
    red_frame = blurred_img[:, :, 1]
    red_histogram = cv.calcHist([red_frame], [0], None, [256], [0, 256])

    global count
    global upsndowns
    avgs.append(round(cv.mean(red_frame)[0]*100))
    upsndowns += "+" if avgs[count] < avgs[count + 1] else "-"
    count += 1

    if upsndowns[-3:] == "+++":
        print("BEAT")

    print(upsndowns)

    axis.cla()
    axis.plot(red_histogram)
    axis.set_xlim([0, 256])
    canvas.draw()

    red_histogram_img = np.array(canvas.renderer.buffer_rgba())

    cv.imshow('Red Histogram', red_histogram_img)
    cv.imshow('Histogram Src', red_frame)


if __name__ == '__main__':
    face_cascade = cv.CascadeClassifier('frontal_face.xml')
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Camera won't open!")
        exit()

    detected_duration = 0
    detected_at = (0, 0)
    detected_at_threshold = 10
    max_detected_duration = 0
    extra_windows_open = False

    while True:
        successful, frame = capture.read()

        if not successful:
            print("Error recieving frame")
            break

        # processing
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = (), ()
        threshold = 5
        while len(faces) > 1:
            faces = face_cascade.detectMultiScale(gray, 1.3, threshold)
            threshold += 1

        if len(faces) > 0:
            x, y, w, h = faces[0]

            center_x = int(x + (w / 2))
            center_y = int(y + (h / 2))
            cv.rectangle(frame, (center_x-1, center_y-1),
                         (center_x+1, center_y+1), (0, 0, 255), 2)

            subframe_start_x = int(x + (w*.3))
            subframe_start_y = int(y + 5)
            subframe_end_x = int(x+(w*.7))
            subframe_end_y = int(y+(h/5))
            cv.rectangle(frame, (subframe_start_x, subframe_start_y),
                         (subframe_end_x, subframe_end_y), (0, 0, 0), 2)

            same_face = abs(detected_at[0] - center_x) < detected_at_threshold and abs(
                detected_at[1] - center_y) < detected_at_threshold

            if same_face:
                detected_duration += 1
            else:
                max_detected_duration = max(
                    detected_duration, max_detected_duration)
                print(max_detected_duration)
                detected_duration = 0
            detected_at = (center_x, center_y)

            radius = int((w+h) / 4)
            red = 255 - (detected_duration * 6)
            green = (detected_duration * 4) - 40
            if green < 255:
                cv.circle(frame, (center_x, center_y),
                          radius, (0, green, red), 2)

                if extra_windows_open:
                    cv.destroyWindow('Red Histogram')
                    cv.destroyWindow('Histogram Src')
                    extra_windows_open = False
            else:
                sub_img = frame[
                    subframe_start_y:subframe_end_y, subframe_start_x:subframe_end_x, :]
                getRedHistogram(sub_img)
                extra_windows_open = True

        cv.imshow('detect_faces', frame)

        if cv.waitKey(30) == ord('q'):
            break

    cv.destroyAllWindows()
    capture.release()
