from PySide6 import QtCore, QtWidgets, QtGui

from ui.simulation_options import SimulationOptionsDialog
from ui.synchronous_generator import SynchronousGeneratorDialog


class ToolbarWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.simulateButton = QtWidgets.QPushButton('Simulate')
        self.optionsButton = QtWidgets.QPushButton('Options')
        self.generatorButton = QtWidgets.QPushButton('Generator Dialog (will be remove)')
        simulate_icon = QtGui.QPixmap(':/simulate_icon.png')
        self.simulateButton.setIcon(QtGui.QIcon(simulate_icon))

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.simulateButton)
        self.layout.addWidget(self.optionsButton)
        self.layout.addWidget(self.generatorButton)

        self.simulateButton.clicked.connect(self.simulate)
        self.optionsButton.clicked.connect(self.openOptionsDialog)
        self.generatorButton.clicked.connect(self.openGeneratorDialog)

    @QtCore.Slot()
    def simulate(self):
        pass

    @QtCore.Slot()
    def openOptionsDialog(self):
        dialog = SimulationOptionsDialog()
        dialog.exec()

    @QtCore.Slot()
    def openGeneratorDialog(self):
        dialog = SynchronousGeneratorDialog()
        dialog.exec()