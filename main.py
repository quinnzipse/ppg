import numpy
import cv2
import matplotlib.pyplot as plt


def show_histogram(input_image):
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histogram = cv2.calcHist([input_image], [i], None, [256], [0, 256])
        plt.plot(histogram, col)
        plt.xlim([0, 256])
    plt.show()


if __name__ == '__main__':
    capture = cv2.VideoCapture(0)
    success, image = capture.read()
    cv2.imshow("Feed", image)

    while cv2.getWindowProperty("Feed", 0) >= 0:
        success, image = capture.read()

        if success:
            b = image[:, :, 0]
            g = image[:, :, 1]
            r = image[:, :, 2]

            show_histogram(image)

            cv2.imshow("Red Feed", r)
            cv2.imshow("Green Feed", g)
            cv2.imshow("Blue Feed", b)

        cv2.waitKey(1)

    cv2.destroyAllWindows()
    capture.release()
