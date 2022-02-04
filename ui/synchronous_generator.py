from PySide6 import QtWidgets, QtCore


class SynchronousGeneratorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SynchronousGeneratorDialog, self).__init__(parent)

        self.setWindowTitle('Synchronous Generator')

        self.simulateButton = QtWidgets.QPushButton('SELECT GENERATOR.CSV')
        self.simulateButton.setStyleSheet('color: blue')

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.simulateButton)

        self.simulateButton.clicked.connect(self.selectFile)

    @QtCore.Slot()
    def selectFile(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select your CSV file", "", "CSV Files (*.csv)", options=options)
        if fileName:
            print(fileName)
