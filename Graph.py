#####
# Class to represent a graph where the nodes are positioned in a circular pattern
# and the edges must arc toward the center of the circle.
#####
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
        for node in self.nodes:
            for edge in node.getOutgoing():
                for otherNode in self.nodes:
                    if (otherNode != edge[0] && otherNode != edge[1]):
                        startBetween = True
                        try:
                            startIndex = self.nodes.index(otherNode, edge[0], edge[1])
                        except ValueError:
                            startBetween = False
                        for otherEdge in otherNode.getOutgoing():
                            endBetween = True
                            try:
                                endIndex = self.nodes.index(otherEdge[1], edge[0], edge[1]
                            except ValueError:
                                endBetween = False
                            if (startBetween != endBetween):
                                crosses += 1
        return crosses
