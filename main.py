import numpy as np
#from scipy import spatial
import cv2
import svgwrite as svg
import time

class Capture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        # cap.set(cv2.CAP_PROP_MODE,cv2.CAP_MODE_YUYV)
        self.cap.set(cv2.CAP_PROP_MODE, 3)

        self.out = cv2.VideoWriter("Vid.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (int(self.cap.get(3)), int(self.cap.get(4))))

    def frame(self, cvt=False):
        ret, f = self.cap.read()
        if cvt: f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
        return f

    def gravar(self, i):
        self.out.write(i)


class Seguimentation:

    def __init__(self, cap):
        self.cap = cap

        self.saida = svg.Drawing('o.svg', size=(800, 640), profile='full')

        self.frameCor = self.cap.frame()

        self.frameo = self.frameCor

        self.subtrac = self.frameo

        self.frameGray = self.frameo

        self.frameBlur = self.frameo

        self.seguimentado = self.frameo

        self.cantos = []

    def loop(self, stop="N"):
        saida = dict()

        self.frameo = self.cap.frame()
        saida["frameo"] = cv2.cvtColor(self.frameo, cv2.COLOR_BGR2RGB)

        if (stop == "frameo"):
            return saida

        self.subtrac = cv2.subtract(self.frameCor, self.frameo)
        saida["subtrac"] = cv2.cvtColor(self.subtrac, cv2.COLOR_BGR2RGB)

        if (stop == "subtrac"):
            return saida

        self.frameGray = cv2.cvtColor(self.subtrac, cv2.COLOR_BGR2GRAY)
        saida["frameGray"] = cv2.cvtColor(self.frameGray, cv2.COLOR_GRAY2BGR)

        if (stop == "frameGray"):
            return saida

        self.frameBlur = cv2.GaussianBlur(self.frameGray, (17, 17), 0)
        saida["frameBlur"] = cv2.cvtColor(self.frameBlur, cv2.COLOR_GRAY2RGB)

        if (stop == "frameBlur"):
            return saida

        _, self.seguimentado = cv2.threshold(self.frameBlur, otsuMod(self.frameBlur, 30), 255, cv2.THRESH_BINARY)
        saida["seguimentado"] = cv2.cvtColor(self.seguimentado, cv2.COLOR_GRAY2RGB)

        if (stop == "seguimentado"):
            return saida

        elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        self.seguimentado = cv2.morphologyEx(self.seguimentado, cv2.MORPH_CLOSE, elemento)
        saida["seguimentado2"] = cv2.cvtColor(self.seguimentado, cv2.COLOR_GRAY2RGB)

        if (stop != "cantos"):
            return saida

        self.cantos = cv2.goodFeaturesToTrack(self.seguimentado, 1000, 0.01, 3)
        if self.cantos is not None:
            self.cantos = np.int0(self.cantos)

            saida["cantos"] = self.order()
        else:
            saida["cantos"] = []

        return saida

    def order(self):
        # a = [(i[0][0], i[0][1]) for i in self.cantos.tolist()]
        #
        # arv = spatial.KDTree(a)
        #
        # v = min(a, key=lambda n: (n[0] + n[1]))
        #
        # b = [list(a[v[1]])]
        #
        # while a:
        #     v = arv.query([v])
        #     arv.data[v[1][0]] = [10000, 10000]
        #     print(b)
        #     b.append([a[v[1][0]][0], a[v[1][0]][1]])
        a = [i[0] for i in self.cantos.tolist()]

        v = min(a, key=lambda n: (n[0] + n[1]))
        a.remove(v)
        b = [v]

        while a:
            v = min(a, key=lambda n: (n[0] - v[0]) ** 2 + (n[1] - v[1]) ** 2)
            a.remove(v)
            b.append(v)

        return b

    def Outline(self):
        self.loop()
        b = self.order()
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
            if k == 27 or cv2.getWindowProperty('Video', 0) == -1:
                break

    except KeyboardInterrupt:
        pass

    instance.cap.release()
    cv2.destroyAllWindows()


class ColorSeg:

    def __init__(self, cap):
        self.cap = cap

        self.frameo = self.cap.frame()
        self.seguimentado = self.frameo

        self.colors = []
        self.color_limits = [0, 180]
        self.masks = []

        self.planoCor = np.zeros(self.frameo.shape, np.uint8)
        self.planoCor[:] = (100, 255, 255)
        self.planoCor = cv2.cvtColor(self.planoCor, cv2.COLOR_HSV2BGR)

    def loop(self):
        saida = dict()

        self.frameo = self.cap.frame()

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

        self.cap.gravar(self.seguimentado)
        saida["Imagem"] = cv2.cvtColor(self.seguimentado, cv2.COLOR_BGR2RGB)
        return saida

    def new_color(self, color):
        hue = 1 if color[0] == 0 else color[0]

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


