from model.element import Element


class TransmissionLine(Element):
    def __init__(self, id):
        super().__init__(2, id)
