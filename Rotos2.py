import numpy as np
import cv2
import svgwrite as svg
import time


class ColorSeg:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_MODE, 3)

        _, self.frameo = self.cap.read()
        self.seguimentado = self.frameo

        self.out = cv2.VideoWriter("Vid.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (int(self.cap.get(3)), int(self.cap.get(4))))

        self.colors = []
        self.color_limits = [0, 180]
        self.masks = []

        self.planoCor = np.zeros(self.frameo.shape, np.uint8)
        self.planoCor[:] = (100, 255, 255)
        self.planoCor = cv2.cvtColor(self.planoCor, cv2.COLOR_HSV2BGR)

    def loop(self):
        ret, self.frameo = self.cap.read()

        img = cv2.cvtColor(cv2.GaussianBlur(self.frameo, (9, 9), 5), cv2.COLOR_BGR2HSV)

        self.seguimentado = np.zeros(self.frameo.shape, np.uint8)
        self.seguimentado[:] = (0, 0, 0)
        self.masks = []



        # Branco
        mask = cv2.inRange(img, (0, 0, 180), (180, 50, 255))
        self.masks.append(mask)

        planoCor = np.zeros(self.frameo.shape, np.uint8)
        planoCor[:] = (255, 255, 255)

        cor = cv2.bitwise_and(planoCor, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR))
        self.seguimentado = cv2.add(self.seguimentado, cor)

        # /Branco

        for i, color in enumerate(self.colors):
            mask = cv2.inRange(img, (int(self.color_limits[i]), 50, 35), (int(self.color_limits[i+1]) -1, 255, 200))
            self.masks.append(mask)

            planoCor = np.zeros(self.frameo.shape, np.uint8)
            planoCor[:] = tuple(color)
            planoCor = cv2.cvtColor(planoCor, cv2.COLOR_HSV2BGR)

            cor = cv2.bitwise_and(planoCor, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR))
            self.seguimentado = cv2.add(self.seguimentado, cor)

        self.out.write(self.seguimentado)

    def new_color(self, color):
        hue = color[0]

        for i, v in enumerate(self.color_limits):
            if hue == v:

                self.colors[i] = color
                break

            if hue > v:
                continue

            self.colors.insert(i, color)
            self.color_limits = [0]
            if len(self.colors) > 1:
                self.color_limits.extend([(self.colors[j-1][0]+v[0])/2 for j, v in enumerate(self.colors[1:])])
            self.color_limits.append(180)
            break

        self.color_limits.sort()
        self.colors.sort(key=lambda a: a[0])

    def reset_color(self):
        self.colors = []
        self.color_limits = [0, 180]


def mouse(evento, x, y, flags, params):

    if evento == cv2.EVENT_LBUTTONDOWN:
        hsv = cv2.cvtColor(instance.frameo, cv2.COLOR_BGR2HSV)
        cor = hsv[y, x, :]
        print(cor)
        instance.new_color(cor)

    if evento == cv2.EVENT_RBUTTONDOWN:
        instance.reset_color()


if __name__ == "__main__":

    instance = ColorSeg()

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
