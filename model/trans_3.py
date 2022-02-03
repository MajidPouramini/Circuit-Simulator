from model.element import Element


class Trans3(Element):
    def __init__(self, id, x, y):
        super().__init__(3, 'trans_3.png', id, x, y)
