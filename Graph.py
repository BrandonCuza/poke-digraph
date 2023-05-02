#####
# Class to represent a graph where the nodes are positioned in a circular pattern
# and the edges must arc toward the center of the circle.
#####

from Node import Node

class Graph:

    def __init__(self):
        self.nodes = []

    def getNodes(self):
        return self.nodes

    def addNode(self, node):
        self.nodes.append(node)

    # Function that returns the number of times edges in the graph cross over
    def getCrosses(self):
        crosses = 0
        nodes = self.nodes
        for node in nodes:
            for edge in node.getOutgoing():
                startIndex = nodes.index(edge[0])
                endIndex = nodes.index(edge[1])
                if endIndex < startIndex:
                    temp = startIndex
                    startIndex = endIndex
                    endIndex = temp
                for otherNode in nodes:
                    if (otherNode != edge[0] and otherNode != edge[1] and nodes.index(otherNode) > nodes.index(node)):
                        otherStartIndex = nodes.index(otherNode)
                        startsBetween = False
                        if (startIndex < otherStartIndex and otherStartIndex < endIndex):
                            startsBetween = True
                        for otherEdge in otherNode.getOutgoing():
                            if nodes.index(otherEdge[1]) > nodes.index(node):
                                otherEndIndex = nodes.index(otherEdge[1])
                                endsBetween = False
                                if (startIndex == otherStartIndex or startIndex == otherEndIndex or endIndex == otherStartIndex or endIndex == otherEndIndex):
                                    break
                                if (startIndex < otherEndIndex and otherEndIndex < endIndex):
                                    endsBetween = True
                                if (startsBetween != endsBetween):
                                    print("Crossover #" +str(crosses + 1) + " between [" + edge[0].getName() + ", " + edge[1].getName() +"] and [" + otherEdge[0].getName() + ", " + otherEdge[1].getName() + "]\n")
                                    crosses += 1
        return crosses
