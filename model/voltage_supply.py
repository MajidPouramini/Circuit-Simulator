from model.element import Element

class VoltageSupply(Element):
    def __init__(self, id):
        super().__init__(2, id)
        