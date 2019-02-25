import numpy as np
import cv2
import svgwrite as svg
import time

frameCor = 0


def mouse(evento, x, y, flags, params):
    global frameCor
    if evento == cv2.EVENT_LBUTTONDOWN:
        frameB = frameo[:, :, 0]
        frameG = frameo[:, :, 1]
        frameR = frameo[:, :, 2]



        try:
            cor = frameo[y, x, :]
            frameCor = frameo

            print(cor)
        except IndexError:
            frameCor[:, :, :] = 255



    if evento == cv2.EVENT_RBUTTONDOWN:
        time.sleep(1)

        a = [i[0] for i in cantos.tolist()]
        a.sort(key=lambda n: (n[0] + n[1]), reverse=True)
        b = []

        while a:
            v = a.pop()
            b.append(v)
            a.sort(key=lambda n: (n[0] - v[0]) ** 2 + (n[1] - v[1]) ** 2, reverse=True)

        linha = svg.shapes.Polyline(points=b, style="fill-opacity:0;", stroke_width="3", stroke="black")
        saida.add(linha)

        saida.save()
        print("Ok")


def otsuMod(img, n):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_norm = hist.ravel() / hist.max()
    Q = hist_norm.cumsum()
    bins = np.arange(256)
    fn_min = np.inf
    thresh = -1
    for i in range(1, 256):
        p1, p2 = np.hsplit(hist_norm, [i])  # probabilities
        q1, q2 = Q[i], Q[255] - Q[i]  # cum sum of classes
        b1, b2 = np.hsplit(bins, [i])  # weights

        m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
        v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2

        fn = v1 * q1 + v2 * q2
        if fn < fn_min:
            fn_min = fn
            thresh = i

    return thresh - n


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_MODE, cv2.CAP_MODE_YUYV)

cv2.namedWindow("Video")
cv2.setMouseCallback("Video", mouse)

saida = svg.Drawing('o.svg', profile='tiny')

_, frameCor = cap.read()

try:
    while 1:
        ret, frameo = cap.read()

        subtrac = cv2.subtract(frameCor, frameo)

        frameGray = cv2.cvtColor(subtrac, cv2.COLOR_RGB2GRAY)

        frameBlur = cv2.GaussianBlur(frameGray, (17, 17), 0)

        _, seguimentado = cv2.threshold(frameBlur, otsuMod(frameBlur, 30), 255, cv2.THRESH_BINARY)

        elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        seguimentado = cv2.morphologyEx(seguimentado, cv2.MORPH_CLOSE, elemento)

        cantos = cv2.goodFeaturesToTrack(seguimentado, 1000, 0.01, 1)
        if cantos is not None: cantos = np.int0(cantos)

        se = cv2.bitwise_and(cv2.cvtColor(seguimentado, cv2.COLOR_GRAY2BGR), frameo)
        frameBlur = cv2.cvtColor(frameBlur, cv2.COLOR_GRAY2BGR)
        Vi1 = np.concatenate((frameo, subtrac), axis=1)
        Vi2 = np.concatenate((frameBlur, se), axis=1)
        Vi = np.concatenate((Vi1, Vi2), axis=0)

        Vi=cv2.resize(Vi, (1300, 700))
        cv2.imshow('Video', Vi)

        k = cv2.waitKey(30)
        if k == 27:
            break

except KeyboardInterrupt:
    pass

cap.release()
cv2.destroyAllWindows()



