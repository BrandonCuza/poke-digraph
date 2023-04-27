import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:

    def __init__(self):

        self.visual = []

    def addEdge(self, a, b):
        temp = [a,b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        nx.draw_circular(G, with_labels = True)
        plt.show()
        
S = GraphVisualization()
# Normal

# Fire
S.addEdge('Fire', 'Grass')
S.addEdge('Fire', 'Ice')
S.addEdge('Fire', 'Bug')
S.addEdge('Fire', 'Steel')

# Water
S.addEdge('Water', 'Fire')
S.addEdge('Water', 'Ground')
S.addEdge('Water', 'Rock')

# Grass
S.addEdge('Grass', 'Water')
S.addEdge('Grass', 'Ground')
S.addEdge('Grass', 'Rock')

# Electric
S.addEdge('Electric', 'Water')
S.addEdge('Electric', 'Flying')

# Ice
S.addEdge('Ice', 'Grass')
S.addEdge('Ice', 'Ground')
S.addEdge('Ice', 'Flying')
S.addEdge('Ice', 'Dragon')

# Fighting
S.addEdge('Fighting', 'Normal')
S.addEdge('Fighting', 'Ice')
S.addEdge('Fighting', 'Rock')
S.addEdge('Fighting', 'Dark')
S.addEdge('Fighting', 'Steel')

#Poison
S.addEdge('Poison', 'Grass')
S.addEdge('Poison', 'Fairy')

# Ground
S.addEdge('Ground', 'Fire')
S.addEdge('Ground', 'Electric')
S.addEdge('Ground', 'Poison')
S.addEdge('Ground', 'Rock')
S.addEdge('Ground', 'Steel')

# Flying
S.addEdge('Flying', 'Grass')
S.addEdge('Flying', 'Fighting')
S.addEdge('Flying', 'Bug')

# Psychic
S.addEdge('Psychic', 'Fighting')
S.addEdge('Psychic', 'Poison')

# Bug
S.addEdge('Bug', 'Grass')
S.addEdge('Bug', 'Psychic')
S.addEdge('Bug', 'Dark')

# Rock
S.addEdge('Rock', 'Fire')
S.addEdge('Rock', 'Ice')
S.addEdge('Rock', 'Flying')
S.addEdge('Rock', 'Bug')

# Ghost
S.addEdge('Ghost', 'Psychic')
S.addEdge('Ghost', 'Ghost')

# Dragon
S.addEdge('Dragon', 'Dragon')

# Dark
S.addEdge('Dark', 'Psychic')
S.addEdge('Dark', 'Ghost')

# Steel
S.addEdge('Steel', 'Ice')
S.addEdge('Steel', 'Rock')
S.addEdge('Steel', 'Fairy')

# Fairy
S.addEdge('Fairy', 'Fighting')
S.addEdge('Fairy', 'Dragon')
S.addEdge('Fairy', 'Dark')

S.visualize()
