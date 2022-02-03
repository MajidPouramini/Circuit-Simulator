from PySide6 import QtCore, QtWidgets, QtGui
from model.circuit import Circuit

from ui.toolbar import ToolbarWidget

class HomeWidget(QtWidgets.QWidget):
    def __init__(self, circuit: Circuit):
        super().__init__()
        self.circut = circuit

        self.toolbar = ToolbarWidget()
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        label = QtWidgets.QLabel(self)
        image = QtGui.QPixmap('transmission_line.png')
        label.setPixmap(image)
                        

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setMenuBar(self.toolbar)
        self.layout.addWidget(label)

    @QtCore.Slot()
    def magic(self):
        self.text.setText('hi')