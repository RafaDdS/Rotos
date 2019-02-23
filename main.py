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

        cor = frameo[y, x, :]

        frameCor = frameo

        print(cor)


    if evento == cv2.EVENT_RBUTTONDOWN:
        time.sleep(1)

        a = [i[0] for i in cantos.tolist() if i[0][0] > 20 and i[0][1] > 20]
        b = []

        while a:
            v = a.pop()
            b.append(v)
            a.sort(key=lambda n: (n[0] - v[0]) ** 2 + (n[1] - v[1]) ** 2, reverse=True)

        linha = svg.shapes.Polyline(points=b, style="fill-opacity:0;", stroke_width="3", stroke="black")
        saida.add(linha)

        saida.save()
        print("Ok")


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_MODE, cv2.CAP_MODE_YUYV)

cv2.namedWindow("Video")
cv2.setMouseCallback("Video", mouse)

saida = svg.Drawing('o.svg', profile='tiny')

_, frameCor = cap.read()

try:
    while 1:
        ret, frameo = cap.read()

        subtrac = cv2.subtract( frameCor , frameo)

        subtrac = cv2.medianBlur(subtrac, 5)

        frameGray = cv2.cvtColor(subtrac, cv2.COLOR_RGB2GRAY)

        _, seguimentado = cv2.threshold(frameGray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
        seguimentado = cv2.morphologyEx(seguimentado, cv2.MORPH_CLOSE, elemento)

        cantos = cv2.goodFeaturesToTrack(seguimentado, 1000, 0.01, 10)
        if cantos is not None: cantos = np.int0(cantos)

        cv2.imshow('Video', frameo)
        cv2.imshow('Seguimentado', seguimentado)

        k = cv2.waitKey(30)
        if k == 27:
            break

except KeyboardInterrupt:
    pass

cap.release()
cv2.destroyAllWindows()
