import json

class FileReader():
    def __init__(self, path):
        self.data = json.load(open(path))
        self.elements = self.data['elements']
        self.wires = self.data['wires']

    def getElements(self):
        return self.elements

    def getWires(self):
        return self.wires