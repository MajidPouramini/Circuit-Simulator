from model.element import Element

class VoltageTrans(Element):
    def __init__(self, id, x, y):
        super().__init__(2, 'voltage_trans.png', id, x, y)
        