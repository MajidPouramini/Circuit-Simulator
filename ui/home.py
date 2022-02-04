from PySide6 import QtCore, QtWidgets, QtGui
from model.circuit import Circuit
from ui.board import BoardWidget
import random

from ui.toolbar import ToolbarWidget

class HomeWidget(QtWidgets.QWidget):
    def __init__(self, circuit: Circuit):
        super().__init__()
        self.circut = circuit
        # self.setStyleSheet('background-color: green')

        self.toolbar = ToolbarWidget()
        self.board = BoardWidget(circuit)
                        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setMenuBar(self.toolbar)
        self.layout.addWidget(self.board)

    @QtCore.Slot()
    def magic(self):
        self.text.setText('hi')