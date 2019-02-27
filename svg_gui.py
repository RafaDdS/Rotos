import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, \
    QHBoxLayout, QPushButton
from PyQt5 import QtSvg
from PyQt5.QtCore import QRect, QSize

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
        self.setGeometry(QRect(100,100,800,640))
        vertical_layout = QVBoxLayout()

        self.central_widget = QtSvg.QSvgWidget()
        self.central_widget.load('o.svg')
        
        self.central_widget.setLayout(vertical_layout)
        self.setCentralWidget(self.central_widget)           

if __name__ == '__main__':
    app = Application()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


