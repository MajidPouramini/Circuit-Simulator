from model.element import Element

class VoltageSupply(Element):
    def __init__(self, id, x, y):
        super().__init__(2, 'voltage_supply.png', id, x, y)
        