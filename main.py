import sys
import PySide6.QtCore
from PySide6 import QtWidgets

from model.circuit import Circuit
from circut_generator import CircuitGenerator
from file_reader import FileReader
from ui.home import HomeWidget

# Prints PySide6 version
print('Pyside version: ', PySide6.__version__)

# Prints the Qt version used to compile PySide6
print('Qt version: ', PySide6.QtCore.__version__)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please specify a circuit file.')
        sys.exit()
    fileReader = FileReader(sys.argv[1])
    circuitGenerator = CircuitGenerator(fileReader.elements, fileReader.wires)
    circuit: Circuit = circuitGenerator.getCircuit();

    app = QtWidgets.QApplication([])

    widget = HomeWidget(circuit)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())