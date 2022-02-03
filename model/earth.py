from model.element import Element

class Earth(Element):
    def __init__(self, id, x, y):
        super().__init__(1, 'earth.png', id, x, y)
        