from model.element import Element


class Trans2(Element):
    def __init__(self, id, x, y):
        super().__init__(2, 'trans_2.png', id, x, y)
