from PySide6 import QtCore, QtWidgets, QtGui

from model.circuit import Circuit
from model.element import Element


class BoardWidget(QtWidgets.QWidget):
    def __init__(self, circuit: Circuit):
        super().__init__()
        self.ciruit = circuit

    def paintEvent(self, e):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.paintBackground(painter)
        self.drawCircuit(painter)
        painter.end()

    def paintBackground(self, painter: QtGui.QPainter):
        painter.setPen(QtCore.Qt.gray)
        screenWidth = self.size().width()
        screenHeight = self.size().height()

        for x in range(0, screenWidth, 10):
            for y in range(0, screenHeight, 10):
                painter.drawPoint(x, y)

    def drawCircuit(self, painter: QtGui.QPainter):
        painter.setPen(QtCore.Qt.black)
        for elementId in self.ciruit.elements:
            element = self.ciruit.elements[elementId]
            x1, y1 = self.getElementCordinate(element)
            painter.drawRect(x1, y1, 100, 60)
            painter.fillRect(x1 + 1, y1 + 1, 98, 58, QtCore.Qt.white)
            painter.drawText(
                x1 + 2, y1 + 12, f'{elementId} - {type(element).__name__}')

        for wireId in self.ciruit.wires:
            wire =  self.ciruit.wires[wireId]
            head = wire.head
            tail = wire.tail
            painter.drawLine(head.x, head.y, tail.x, tail.y)

    def getElementCordinate(self, element: Element):
        return element.x - 50, element.y - 30
