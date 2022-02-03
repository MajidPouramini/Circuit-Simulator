from model.element import Element


from model.element import Element

class Bus(Element):
    def __init__(self, id, x, y):
        super().__init__(8, 'bus.png', id, x, y)
