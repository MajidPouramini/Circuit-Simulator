from tokenize import Number
from typing import List

import model.wire as wire


class Element():
    terminals: List[wire.Wire] = []

    def __init__(self, number_of_terminals: Number, id: Number, x: Number, y: Number):
        self.number_of_terminals = number_of_terminals
        self.id = id
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.id == other.id

    def addTerminal(self, wire: wire.Wire):
        if len(self.terminals) < self.number_of_terminals:
            self.terminals.append(wire)
        else: raise Exception('Number of terminals is ' + self.number_of_terminals + '. It cannot add more than that.')

    def removeTerminalByIndex(self, index: Number):
        if 0 <= index < self.number_of_terminals:
            self.terminals.pop(index)
        else: raise Exception('Index out of bound (number of terminals: ' + self.number_of_terminals + ').')

    def removeTerminal(self, wire: wire.Wire):
        self.terminals.remove(wire)

    
        