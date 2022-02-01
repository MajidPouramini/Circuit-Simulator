
class Wire():
    # head and tail must be elements
    def __init__(self, head, tail):
        import model.element as element
        self.head: element.Element = head
        self.tail: element.Element = tail
