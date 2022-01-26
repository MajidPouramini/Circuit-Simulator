from PySide6 import QtCore, QtWidgets

class ToolbarWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.simulateButton = QtWidgets.QPushButton("Simulate")
        self.optionsButton = QtWidgets.QPushButton("Options")

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.simulateButton)
        self.layout.addWidget(self.optionsButton)
    
        self.simulateButton.clicked.connect(self.simulate)
        self.optionsButton.clicked.connect(self.simulate)

    @QtCore.Slot()
    def simulate(self):
        pass

    @QtCore.Slot()
    def openOptionsDialog():
        pass