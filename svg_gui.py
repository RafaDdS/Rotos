import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, \
    QHBoxLayout, QPushButton
from PyQt5 import QtSvg
from PyQt5.QtCore import QRect, QSize, Qt, QTimer
from PyQt5.QtGui import QPainter, QPen
from main import Seguimentation

__all__ = ['Application', 'MainWindow']


class Application(QApplication):
    """
    Main application class
    """

    def __init__(self):
        super().__init__(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(QRect(100, 100, 800, 640))
        vertical_layout = QVBoxLayout()

        self.central_widget = QtSvg.QSvgWidget()
        self.central_widget.load('o.svg')

        self.central_widget.setLayout(vertical_layout)
        self.setCentralWidget(self.central_widget)


class Lines(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle("Ao vivo")
        self.show()



    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        # self.timer = QTimer()
        # self.timer.timeout.connect()
        # self.timer.start(100)
        self.drawLines(qp)
        qp.end()



    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)

        cantos = instance.loop()
        print(cantos)

        if cantos:
            last = []
            for i in cantos:
                if last:
                    qp.drawLine(last[0][0], last[0][1], i[0][0], i[0][1])
                last = i




if __name__ == '__main__':
    instance = Seguimentation()
    app = Application()
    window = MainWindow()
    window.show()
    l = Lines()
    sys.exit(app.exec_())

