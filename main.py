from matplotlib.figure import Figure
import numpy as np
import cv2 as cv
import time
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas

if __name__ == '__main__':

    # Setup matplotlib here
    fig = Figure()
    canvas = FigureCanvas(fig)
    axis = fig.subplots()
    axis.set_title("Histogram")

    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Camera won't open!")
        exit()

    while True:
        successful, frame = capture.read()

        if not successful:
            print("Error recieving frame")
            break

        red_frame = frame[:,:,2]
        red_histogram = cv.calcHist([red_frame], [0], None, [256], [0, 256])

        axis.cla()
        axis.plot(red_histogram)
        axis.set_xlim([0,256])
        canvas.draw()

        red_histogram_img = np.array(canvas.renderer.buffer_rgba())

        cv.imshow('Red Histogram', red_histogram_img)
        cv.imshow('video', frame)
        
        if cv.waitKey(25) == ord('q'):
            break
        
    cv.destroyAllWindows()
    capture.release()
