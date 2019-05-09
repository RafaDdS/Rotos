from main_GUI import Ui_Rotos
import PyQt5 as n
from PyQt5 import QtSvg
from main import Seguimentation, ColorSeg, Capture
import numpy as np


color = n.QtGui.QColor("green")

def NewColor(AAA):
    palette = n.QtGui.QPalette()

    brush = n.QtGui.QBrush(AAA)
    brush.setStyle(n.QtCore.Qt.SolidPattern)
    palette.setBrush(n.QtGui.QPalette.Active, n.QtGui.QPalette.Base, brush)

    brush = n.QtGui.QBrush(AAA)
    brush.setStyle(n.QtCore.Qt.SolidPattern)
    palette.setBrush(n.QtGui.QPalette.Inactive, n.QtGui.QPalette.Base, brush)

    brush = n.QtGui.QBrush(AAA)
    brush.setStyle(n.QtCore.Qt.SolidPattern)
    palette.setBrush(n.QtGui.QPalette.Disabled, n.QtGui.QPalette.Base, brush)
    return palette


class ui_mod(Ui_Rotos):

    def __init__(self, R):
        self.graphicsView = n.QtSvg.QSvgWidget(R)
        super().setupUi(R)
        self.cap = Capture()

        self.instance = Seguimentation(self.cap)
        self.instance2 = ColorSeg(self.cap)
        self.dados = self.instance.loop()
        self.dados2 = self.instance2.loop()

        self.graphicsView.load('o.svg')

        self.pushButton.setText("Excluir Background")
        self.pushButton.clicked.connect(lambda: self.instance.ExcludeBackground())
        self.pushButton_2.setText("Salvar Outline")
        self.pushButton_2.clicked.connect(lambda: (self.instance.Outline(), self.graphicsView.load('o.svg')))
        self.pushButton_4.setText("Limpar cores")
        self.pushButton_4.clicked.connect(lambda: (self.instance2.reset_color(), self.comboBox_2.clear()))

        self.pushButton_5.clicked.connect(lambda: self.comboBox_2.removeItem(self.comboBox_2.currentIndex()))
        self.pushButton_6.clicked.connect(self.colorPicker)

        self.timer = n.QtCore.QTimer()
        self.timer.timeout.connect(self.atualizar_imagens)
        self.timer.start(10)

        self.horizontalSlider.valueChanged.connect(lambda: self.lineEdit.setText(str(self.horizontalSlider.value())))
        self.horizontalSlider_2.valueChanged.connect(lambda: self.lineEdit_2.setText(str(self.horizontalSlider_2.value())))
        self.horizontalSlider_3.valueChanged.connect(lambda: self.lineEdit_3.setText(str(self.horizontalSlider_3.value())))
        self.horizontalSlider_4.valueChanged.connect(lambda: self.lineEdit_4.setText(str(self.horizontalSlider_4.value())))
        self.horizontalSlider_5.valueChanged.connect(lambda: self.lineEdit_5.setText(str(self.horizontalSlider_5.value())))
        self.plainTextEdit.setPalette(NewColor(color))

        self.graphicsView_2.mousePressEvent = self.getPixel

    def getPixel(self, event):
        xx = event.pos().x()
        yy = event.pos().y()
        cc = self.qimg.pixel(xx, yy)
        c_obj = n.QtGui.QColor(cc)
        self.comboBox_2.addItem(c_obj.name())
        self.plainTextEdit.setPalette(NewColor(c_obj))
        self.comboBox_2.setCurrentIndex(self.comboBox_2.count()-1)

        c_obj = c_obj.toHsv()
        self.instance2.new_color(np.array([c_obj.hsvHue(), c_obj.hsvSaturation(), 120]))   ## Corrigir

    def atualizar_imagens(self):
        if str(self.comboBox.currentText()) == "CodigoCor":
            self.dados2 = self.instance2.loop()
        else:
            self.dados = self.instance.loop(str(self.comboBox.currentText()))


        scene = n.QtWidgets.QGraphicsScene()
        self.qimg = converter_imagem(self.cap.frame(True))
        pixmap = n.QtGui.QPixmap.fromImage(self.qimg)
        scene.addPixmap(pixmap)
        self.graphicsView_2.setScene(scene)

        scene = n.QtWidgets.QGraphicsScene()

        if str(self.comboBox.currentText()) == "CodigoCor":
            qimg = converter_imagem(self.dados2["Imagem"])
        else:
            qimg = converter_imagem(self.dados[str(self.comboBox.currentText())])

        pixmap = n.QtGui.QPixmap.fromImage(qimg)
        scene.addPixmap(pixmap)
        self.graphicsView_3.setScene(scene)

    def colorPicker(self):
        color = n.QtWidgets.QColorDialog.getColor()
        self.plainTextEdit.setPalette(NewColor(color))
        self.comboBox_2.setItemText(self.comboBox_2.currentIndex(), color.name())

def converter_imagem(cvImg):
    height, width, channel = cvImg.shape
    bytesPerLine = 3 * width
    return n.QtGui.QImage(cvImg.data, width, height, bytesPerLine, n.QtGui.QImage.Format_RGB888)

if __name__ == "__main__":
    import sys
    app = n.QtWidgets.QApplication(sys.argv)
    Rotos = n.QtWidgets.QWidget()
    ui = ui_mod(Rotos)
    Rotos.show()
    sys.exit(app.exec_())