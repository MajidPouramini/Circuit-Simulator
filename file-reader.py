import json

def fileReader(path):
    file = open(path)
    data = json.load(file)

    elements = extractElements(data)
    wires = extractWires(data)

def extractElements(data):
    for element in data['elements']:
        # create element
        print(element)

def extractWires(data):
    for wire in data['wires']:
        # creat wire
        print(wire)

fileReader('./sample.json')