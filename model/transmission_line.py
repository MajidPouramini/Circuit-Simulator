from model.element import Element


class TransmissionLine(Element):
    def __init__(self, id, x, y):
        super().__init__(2, 'transmission_line.png', id, x, y)
