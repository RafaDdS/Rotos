import numpy as np
import cv2
from main import ColorSeg, Capture
import svgwrite as svg
import time


def mouse(evento, x, y, flags, params):

    if evento == cv2.EVENT_LBUTTONDOWN:
        hsv = cv2.cvtColor(instance.frameo, cv2.COLOR_BGR2HSV)
        cor = hsv[y, x, :]
        print(cor)

        instance.new_color(cor)

    if evento == cv2.EVENT_RBUTTONDOWN:
        instance.reset_color()


if __name__ == "__main__":

    instance = ColorSeg(Capture())

    cv2.namedWindow("Video")
    cv2.setMouseCallback("Video", mouse)

    try:
        while 1:
            instance.loop()

            if instance.masks:
                Vi = np.concatenate((instance.frameo, instance.seguimentado), axis=1)

            else:
                Vi = instance.frameo

            cv2.imshow('Video', Vi)

            k = cv2.waitKey(1)
            if k == 27 or cv2.getWindowProperty('Video', 0) == -1:
                break

    except KeyboardInterrupt:
        pass

    instance.cap.release()
    instance.out.release()
    cv2.destroyAllWindows()
