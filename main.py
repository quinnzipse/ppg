import numpy
import cv2
import time
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


fig, axs = plt.subplots(ncols=1, nrows=2)
ax0 = axs[0]
ax1 = axs[1]
capture = cv2.VideoCapture(0)

def animate(nothing):
        success, img = capture.read()
        data = [0, 256]
        for i in range(0, 200):
            for x in range(0, 200):
                data.append(img[x, i, 2])
        ax1.cla()
        ax1.imshow(img)
        ax0.cla()
        ax0.hist(data, bins = 32, edgecolor="black", log=True)

if __name__ == '__main__':
    _animation = animation.FuncAnimation(fig, animate, interval=50)
    
    plt.tight_layout()
    plt.show()
    cv2.destroyAllWindows()

    capture.release()
