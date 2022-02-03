from PySide6 import QtCore, QtWidgets, QtGui

from ui.simulation_options import SimulationOptionsDialog

class ToolbarWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.simulateButton = QtWidgets.QPushButton("Simulate")
        self.optionsButton = QtWidgets.QPushButton("Options")
        simulate_icon = QtGui.QPixmap("../assets/icons/simulate_icon.png")
        self.simulateButton.setIcon(QtGui.QIcon(simulate_icon))

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.simulateButton)
        self.layout.addWidget(self.optionsButton)
    
        self.simulateButton.clicked.connect(self.simulate)
        self.optionsButton.clicked.connect(self.openOptionsDialog)

    @QtCore.Slot()
    def simulate(self):
        pass

    @QtCore.Slot()
    def openOptionsDialog(self):
        dialog = SimulationOptionsDialog()
        dialog.exec()