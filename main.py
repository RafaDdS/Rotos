import numpy as np
import cv2
import svgwrite as svg
import time
import  asyncio


class Seguimentation:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        # cap.set(cv2.CAP_PROP_MODE,cv2.CAP_MODE_YUYV)
        self.cap.set(cv2.CAP_PROP_MODE, 3)

        self.saida = svg.Drawing('o.svg', size=(800, 640), profile='full')

        _, self.frameCor = self.cap.read()

        self.frameo = self.frameCor

        self.subtrac = self.frameo

        self.frameGray = self.frameo

        self.frameBlur = self.frameo

        self.seguimentado = self.frameo

        self.cantos = []



    def loop(self):
        ret, self.frameo = self.cap.read()

        self.subtrac = cv2.subtract(self.frameCor, self.frameo)

        self.frameGray = cv2.cvtColor(self.subtrac, cv2.COLOR_RGB2GRAY)

        self.frameBlur = cv2.GaussianBlur(self.frameGray, (17, 17), 0)

        _, self.seguimentado = cv2.threshold(self.frameBlur, otsuMod(self.frameBlur, 30), 255, cv2.THRESH_BINARY)

        elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        self.seguimentado = cv2.morphologyEx(self.seguimentado, cv2.MORPH_CLOSE, elemento)

        self.cantos = cv2.goodFeaturesToTrack(self.seguimentado, 1000, 0.01, 1)
        if self.cantos is not None: cantos = np.int0(self.cantos)

        print(cantos)

    def Outline(self):
        a = [i[0] for i in self.cantos.tolist()]
        a.sort(key=lambda n: (n[0] + n[1]), reverse=True)
        b = []

        while a:
            v = a.pop()
            b.append(v)
            a.sort(key=lambda n: (n[0] - v[0]) ** 2 + (n[1] - v[1]) ** 2, reverse=True)

        linha = svg.shapes.Polyline(points=b, style="fill-opacity:0;", stroke_width="3", stroke="black")
        self.saida.add(linha)

        self.saida.save()
        print("Ok")

    def ExcludeBackground(self):
        try:
            self.frameCor = self.frameo
        except IndexError:
            self.frameCor[:, :, :] = 255


def mouse(evento, x, y, flags, params):
    global frameCor
    if evento == cv2.EVENT_LBUTTONDOWN:
        instance.ExcludeBackground()
        cor = instance.frameo[y, x, :]
        print(cor)

    if evento == cv2.EVENT_RBUTTONDOWN:
        time.sleep(1)

        instance.Outline()




def otsuMod(img, n):

    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_norm = hist.ravel() / hist.max()
    Q = hist_norm.cumsum()
    bins = np.arange(256)
    fn_min = np.inf
    thresh = -1
    for i in range(1, 256):
        p1, p2 = np.hsplit(hist_norm, [i])
        q1, q2 = Q[i], Q[255] - Q[i]
        b1, b2 = np.hsplit(bins, [i])

        m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
        v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2

        fn = v1 * q1 + v2 * q2
        if fn < fn_min:
            fn_min = fn
            thresh = i

    return thresh - n


if __name__ == "__main__":

    instance = Seguimentation()

    cv2.namedWindow("Video")
    cv2.setMouseCallback("Video", mouse)

    try:
        while 1:
            instance.loop()

            se = cv2.bitwise_and(cv2.cvtColor(instance.seguimentado, cv2.COLOR_GRAY2BGR), instance.frameo)
            frameBlur = cv2.cvtColor(instance.frameBlur, cv2.COLOR_GRAY2BGR)
            Vi1 = np.concatenate((instance.frameo, instance.subtrac), axis=1)
            Vi2 = np.concatenate((frameBlur, se), axis=1)
            Vi = np.concatenate((Vi1, Vi2), axis=0)

            Vi = cv2.resize(Vi, (1300, 700))
            cv2.imshow('Video', Vi)

            k = cv2.waitKey(30)
            if k == 27:
                break

    except KeyboardInterrupt:
        pass

    instance.cap.release()
    cv2.destroyAllWindows()
