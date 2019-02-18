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
        print(cor)

        frameCor.fill(0)

        frameCor[np.where((frameCor == cor).all(axis=2))] = [0, 170, 0]

        # frameCor = np.float64(frameCor)
        # for i, v in enumerate(cor):
        #    frameCor = frameo[:, :, i] * v * 0.00130718954248366

    if evento == cv2.EVENT_RBUTTONDOWN:
        time.sleep(1)

        a = [i[0] for i in cantos.tolist() if i[0][0] > 20 and i[0][1] > 20]
        b = []

        while a:
            v = a.pop()
            b.append(v)
            a.sort(key=lambda n: (n[0] - v[0]) ** 2 + (n[1] - v[1]) ** 2, reverse=True)

        linha = svg.shapes.Polyline(points=b)
        saida.add(linha)

        saida.save()
        print("Ok")


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_MODE, cv2.CAP_MODE_YUYV)

cv2.namedWindow("Video")
cv2.setMouseCallback("Video", mouse)

saida = svg.Drawing('test.svg', profile='tiny')

_, frameCor = cap.read()

try:
    while 1:
        ret, frameo = cap.read()

        frameGray = cv2.cvtColor(frameo, cv2.COLOR_RGB2GRAY)

        frameGray = np.float32(frameGray)

        cantos = cv2.goodFeaturesToTrack(frameGray, 1000, 0.01, 10)
        cantos = np.int0(cantos)

        seguimentado = cv2.threshold(frameCor, 0.1, 255, cv2.THRESH_BINARY)

        cv2.imshow('Video', frameo)
        cv2.imshow('Seguimentado', frameCor)

        k = cv2.waitKey(30)
        if k == 27:
            break

except KeyboardInterrupt:
    pass

cap.release()
cv2.destroyAllWindows()
