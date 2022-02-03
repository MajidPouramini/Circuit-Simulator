from model.element import Element

class CurrentTrans(Element):
    def __init__(self, id, x, y):
        super().__init__(2, 'current_trans.png', id, x, y)
        