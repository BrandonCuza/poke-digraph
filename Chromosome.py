#####
# Class to represent a graph where the nodes are positioned in a circular pattern
# and the edges must arc toward the center of the circle.
#####

from Node import Node

class Chromosome:

    def __init__(self, nodes):
        self.nodes = nodes
        self.fitness = self.getCrosses()

    def getNodes(self):
        return self.nodes

    def addNode(self, node):
        self.nodes.append(node)

    def getFitness(self):
        return self.fitness

    def updateFitness(self):
        self.fitness = self.getCrosses()

    # Function that returns the number of times edges in the graph cross over.
    # This acts as the measure of fitness for the evolutionary algorithm.
    def getCrosses(self):
        crosses = 0
        nodes = self.nodes
        
        for node in nodes:
            for edge in  node.getOutgoing():
                edgeHead = nodes.index(node)
                edgeTail = nodes.index(edge[1])

                # Edge is a loop and therefore can always be made to not intersect other edges
                if edgeHead == edgeTail:
                    continue

                # Edges between adjacent vertices cannot intersect other edges
                elif (edgeHead - edgeTail == 1 or edgeHead - edgeTail == -1 or edgeHead - edgeTail == -(len(nodes)-1)):
                    continue
                
                # This undirects the edge for easier processing
                elif edgeTail < edgeHead:
                    temp = edgeHead
                    edgeHead = edgeTail
                    edgeTail = temp
                
                for otherNode in nodes:

                    # Ignore the nodes we are currently looking at (both sides of the edge)
                    if otherNode != node and otherNode != edge[1]:
                        for otherEdge in otherNode.getOutgoing():
                            otherEdgeHead = nodes.index(otherNode)
                            otherEdgeTail = nodes.index(otherEdge[1])

                            # Edge is a loop (see above)
                            if otherEdgeHead == otherEdgeTail:
                                continue

                            # Undirect edge (see above)
                            elif otherEdgeTail < otherEdgeHead:
                                temp = otherEdgeHead
                                otherEdgeHead = otherEdgeTail
                                otherEdgeTail = temp

                            # Edges intersect iff the vertices of the edges are interwoven
                            if ((edgeHead < otherEdgeHead and otherEdgeHead < edgeTail and edgeTail < otherEdgeTail) or (otherEdgeHead < edgeHead and edgeHead < otherEdgeTail and otherEdgeTail < edgeTail)):
                                crosses += 1
        
        return 400 - int(crosses/2)
