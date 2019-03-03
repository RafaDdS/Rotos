import numpy as np
import cv2
from matplotlib import pyplot as plt
import svgwrite as svg
import time


class ColorSeg:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_MODE, 3)

        _, self.frameCor = self.cap.read()

        self.frameo = self.frameCor

        self.subtrac = self.frameo

        self.frameGray = self.frameo

        self.frameBlur = self.frameo

        img = cv2.cvtColor(self.frameo, cv2.COLOR_BGR2HSV)
        self.hist = cv2.calcHist([img], [0], None, [256], [0, 256])


    def loop(self):
        ret, self.frameo = self.cap.read()

        img = cv2.cvtColor(self.frameo, cv2.COLOR_BGR2HSV)
        self.hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
        plt.subplot(121), plt.imshow(img, 'gray')
        plt.subplot(122), plt.hist(self.hist, 256, [0, 256])
        plt.show()

        self.frameBlur = cv2.GaussianBlur(self.frameGray, (17, 17), 0)

        # elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        # self.seguimentado = cv2.morphologyEx(self.seguimentado, cv2.MORPH_CLOSE, elemento)


def mouse(evento, x, y, flags, params):
    global frameCor
    if evento == cv2.EVENT_LBUTTONDOWN:

        cor = instance.frameo[y, x, :]
        print(cor)


if __name__ == "__main__":

    instance = ColorSeg()

    try:
        while 1:
            instance.loop()

            # cv2.imshow('Video', instance.hist)

            k = cv2.waitKey(30)
            if k == 27:
                break

    except KeyboardInterrupt:
        pass

    instance.cap.release()
    cv2.destroyAllWindows()
