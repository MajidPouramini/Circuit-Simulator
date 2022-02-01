class Element():
    terminals = []

    def __init__(self, number_of_terminals, id):
        self.number_of_terminals = number_of_terminals
        self.id = id

    def __eq__(self, other):
        return self.id == other.id

    def addTerminal(self, wire):
        if len(self.terminals) < self.number_of_terminals:
            self.terminals.append(wire)
        else: raise Exception('Number of terminals is ' + self.number_of_terminals + '. It cannot add more than that.')

    def removeTerminalByIndex(self, index):
        if 0 <= index < self.number_of_terminals:
            self.terminals.pop(index)
        else: raise Exception('Index out of bound (number of terminals: ' + self.number_of_terminals + ').')

    def removeTerminal(self, wire):
        self.terminals.remove(wire)

    
        