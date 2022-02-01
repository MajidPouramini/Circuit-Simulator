from tokenize import Number
from typing import Dict

from model.element import Element
from model.wire import Wire


class Circuit():
    def __init__(self):
        self.elements: Dict[Number, Element] = dict()
        self.wires: Dict[Number, Wire] = dict()

    def addWire(self, id, wire):
        self.wires[id] = wire

    def addElement(self, id, element):
        self.elements[id] = element

    def getElement(self, id) -> Element:
        return self.elements[id]

    def getWire(self, id) -> Element:
        return self.wires[id]
