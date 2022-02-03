from PySide6 import QtCore, QtWidgets

class SimulationOptionsDialog(QtWidgets.QDialog):
    comboBoxItems = ['s', 'ms', 'μs', 'ns']

    def __init__(self, parent=None):
        super(SimulationOptionsDialog, self).__init__(parent)

        self.setWindowTitle('Simulation Options')

        # Main Time Step
        self.mainTimeStep = {
            'text': QtWidgets.QLabel('Main Time Step (dt)'),
            'formField': QtWidgets.QLineEdit(),
            'comboBox': QtWidgets.QComboBox()
        }
        self.mainTimeStep['comboBox'].addItems(self.comboBoxItems)

        # Simulation Time
        self.simulationTime = {
            'text': QtWidgets.QLabel('Simulation Time'),
            'formField': QtWidgets.QLineEdit(),
            'comboBox': QtWidgets.QComboBox()
        }
        self.simulationTime['comboBox'].addItems(self.comboBoxItems)

        # Action Buttons
        self.okButton = QtWidgets.QPushButton('Ok')
        self.cancelButton = QtWidgets.QPushButton('Cancel')
    
        self.okButton.clicked.connect(self.onOkClick)
        self.cancelButton.clicked.connect(self.onCancelClick)

        # Dialog layout
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setVerticalSpacing(20)
        self.layout.addWidget(self.mainTimeStep['text'], 0, 0)
        self.layout.addWidget(self.mainTimeStep['formField'], 0, 1)
        self.layout.addWidget(self.mainTimeStep['comboBox'], 0, 2)
        self.layout.addWidget(self.simulationTime['text'], 1, 0)
        self.layout.addWidget(self.simulationTime['formField'], 1, 1)
        self.layout.addWidget(self.simulationTime['comboBox'], 1, 2)
        self.layout.addWidget(self.okButton, 2, 0)
        self.layout.addWidget(self.cancelButton, 2, 1)

    @QtCore.Slot()
    def onOkClick(self):
        self.close()

    @QtCore.Slot()
    def onCancelClick(self):
        self.close()