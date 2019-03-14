from main_GUI import Ui_Rotos
import PyQt5 as n
from main import Seguimentation

class ui_mod(Ui_Rotos):

    def __init__(self, R):
        super().setupUi(R)
        self.instance = Seguimentation()
        self.dados = self.instance.loop()

        self.pushButton.setText("Excluir Background")
        self.pushButton.clicked.connect(lambda: self.instance.ExcludeBackground())
        self.pushButton.setText("Salvar Outline")
        self.pushButton_2.clicked.connect(lambda: self.instance.Outline())

        self.timer = n.QtCore.QTimer()
        self.timer.timeout.connect(self.atualizar_imagens)
        self.timer.start(10)

    def atualizar_imagens(self):
        self.dados = self.instance.loop()

        scene = n.QtWidgets.QGraphicsScene()
        qimg = converer_imagem(self.dados["frameo"])
        pixmap = n.QtGui.QPixmap.fromImage(qimg)
        scene.addPixmap(pixmap)
        self.graphicsView_2.setScene(scene)

        scene = n.QtWidgets.QGraphicsScene()
        qimg = converer_imagem(self.dados["seguimentado"])
        pixmap = n.QtGui.QPixmap.fromImage(qimg)
        scene.addPixmap(pixmap)
        self.graphicsView_3.setScene(scene)


def converer_imagem(cvImg):
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