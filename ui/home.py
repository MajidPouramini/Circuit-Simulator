from PySide6 import QtCore, QtWidgets, QtGui

from ui.toolbar import ToolbarWidget

class HomeWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.toolbar = ToolbarWidget()
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setMenuBar(self.toolbar)
        self.layout.addWidget(self.text)

    @QtCore.Slot()
    def magic(self):
        self.text.setText('hi')