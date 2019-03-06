# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(484, 603)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(80, 250, 332, 170))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalSlider = QtWidgets.QSlider(self.widget_3)
        self.horizontalSlider.setMinimum(-6)
        self.horizontalSlider.setMaximum(80)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setProperty("value", 5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.widget_3)
        self.horizontalSlider_2.setMinimum(-6)
        self.horizontalSlider_2.setMaximum(80)
        self.horizontalSlider_2.setPageStep(5)
        self.horizontalSlider_2.setProperty("value", 5)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_3.addWidget(self.horizontalSlider_2)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.widget_3)
        self.horizontalSlider_3.setMinimum(-6)
        self.horizontalSlider_3.setMaximum(80)
        self.horizontalSlider_3.setPageStep(5)
        self.horizontalSlider_3.setProperty("value", 5)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout_3.addWidget(self.horizontalSlider_3)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.widget_3)
        self.horizontalSlider_4.setMinimum(-6)
        self.horizontalSlider_4.setMaximum(80)
        self.horizontalSlider_4.setPageStep(5)
        self.horizontalSlider_4.setProperty("value", 5)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.verticalLayout_3.addWidget(self.horizontalSlider_4)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.widget_3)
        self.horizontalSlider_5.setMinimum(-6)
        self.horizontalSlider_5.setMaximum(80)
        self.horizontalSlider_5.setPageStep(5)
        self.horizontalSlider_5.setProperty("value", 5)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.verticalLayout_3.addWidget(self.horizontalSlider_5)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        self.horizontalSlider.valueChanged.connect(self.setline1)
        self.horizontalSlider_2.valueChanged.connect(self.setline2)
        self.horizontalSlider_3.valueChanged.connect(self.setline3)
        self.horizontalSlider_4.valueChanged.connect(self.setline4)
        self.horizontalSlider_5.valueChanged.connect(self.setline5)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def setline1(self):
        self.lineEdit.setText(str(self.horizontalSlider.value()))
    def setline2(self):
        self.lineEdit_2.setText(str(self.horizontalSlider_2.value()))
    def setline3(self):
        self.lineEdit_3.setText(str(self.horizontalSlider_3.value()))
    def setline4(self):
        self.lineEdit_4.setText(str(self.horizontalSlider_4.value()))
    def setline5(self):
        self.lineEdit_5.setText(str(self.horizontalSlider_5.value()))



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Red Butao"))
        self.label.setText(_translate("Form", "filtro 1"))
        self.label_2.setText(_translate("Form", "filtro 2"))
        self.label_3.setText(_translate("Form", "filtro 3"))
        self.label_4.setText(_translate("Form", "filtro 4"))
        self.label_5.setText(_translate("Form", "filtro 5"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
