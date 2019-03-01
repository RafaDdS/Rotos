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
        self.setWindowTitle('Pen styles')
        self.show()

        self.timer = QTimer()
        # self.timer.timeout.connect(instance.loop)
        self.timer.start(100)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)

        cantos = [[200, 456], [250, 156], [20, 56], [600, 852]]
        last = []
        for i in cantos:
            if not last:
                last = i
                continue

            qp.drawLine(last[0], last[1], i[0], i[1])
            last = i


if __name__ == '__main__':
    instance = Seguimentation()
    app = Application()
    window = MainWindow()
    window.show()
    l = Lines()
    sys.exit(app.exec_())