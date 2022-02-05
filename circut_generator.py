from typing import Any, List
from model.bus import Bus
from model.wire import Wire
from model.current_trans import CurrentTrans
from model.circuit import Circuit
from model.earth import Earth
from model.element import Element
from model.trans_3 import Trans3
from model.trans_2 import Trans2
from model.transmission_line import TransmissionLine
from model.voltage_supply import VoltageSupply
from model.voltage_trans import VoltageTrans


class CircuitGenerator():
    def __init__(self, elements, wires):
        self.circuit = Circuit()
        for element in elements:
            self.circuit.addElement(element['id'], self.element_factory(element))
        for idx, wire in enumerate(wires):
            self.circuit.addWire(idx, Wire(self.circuit.getElement(wire['from']), self.circuit.getElement(wire['to'])))
            
    def getCircuit(self):
        return self.circuit
        

    def element_factory(self, element_data) -> Element:
        if element_data['name'] == "bus":
            return Bus(element_data['id'], element_data['x'], element_data['y'])
        elif element_data['name'] == "current_trans":
            return CurrentTrans(element_data['id'], element_data['x'], element_data['y'])
        elif element_data['name'] == "earth":
            return Earth(element_data['id'], element_data['x'], element_data['y'])
        elif element_data['name'] == "trans_2":
            return Trans2(element_data['id'], element_data['x'], element_data['y'])
        elif element_data['name'] == "trans_3":
            return Trans3(element_data['id'], element_data['x'], element_data['y'])
        elif element_data['name'] == "transmission_line":
            return TransmissionLine(element_data['id'], element_data['x'], element_data['y'])
        elif element_data['name'] == "voltage_supply":
            return VoltageSupply(element_data['id'], element_data['x'], element_data['y'])
        elif element_data['name'] == "voltage_trans":
            return VoltageTrans(element_data['id'], element_data['x'], element_data['y'])
        else: raise Exception('model ' + element_data + ' is not supported')
            
        
        