class Node:
    instances = []
    
    def __init__(self, name):
        self.name = name
        self.outgoing = []
        self.__class__.instances.append(self)

    def getName(self):
        return self.name

    def getOutgoing(self):
        return self.outgoing

    def addOutgoing(self, node):
        edge = [self, node]
        self.outgoing.append(edge)
