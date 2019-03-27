self.comboBox.addItem("")
self.comboBox.setItemText(0, _translate("Rotos", "subtrac"))
self.comboBox.addItem("")
self.comboBox.setItemText(1, _translate("Rotos", "subtrac"))




def NewColor(C1, C2, C3):
	palette = QtGui.QPalette()

	brush = QtGui.QBrush(QtGui.QColor(C1, C2, C3))
	brush.setStyle(QtCore.Qt.SolidPattern)
	palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)

	brush = QtGui.QBrush(QtGui.QColor(C1, C2, C3))
	brush.setStyle(QtCore.Qt.SolidPattern)
	palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)

	brush = QtGui.QBrush(QtGui.QColor(C1, C2, C3))
	brush.setStyle(QtCore.Qt.SolidPattern)
	palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
return palette

self.plainTextEdit.setPalette(NewColor(C1, C2, C3))

.\env\Scripts\activate