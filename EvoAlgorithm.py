from Chromosome import Chromosome
from Node import Node
import random

numPop = 1000
numGen = 1000

# Function that takes two parents and returns two children created through
# cycle crossover.               
def cycleCross(parent1, parent2):
    parent1 = parent1.getNodes()
    parent2 = parent2.getNodes()

    columns = columnize(parent1, parent2)

    cycles = []
    for column in columns:

        # Check if the column is already in a cycle
        skip = False
        for cycle in cycles:
            if column in cycle:
                skip = True

        # If not, it is the head of a new cycle     
        if not skip:
            head = column[1]
            nextType = column[2]
            cycle = [column]
            # Find columns in this cycle, end when the next type is the same as the head
            while nextType != head:
                for otherColumn in columns:
                    if otherColumn[1] == nextType:
                        cycle.append(otherColumn)
                        nextType = otherColumn[2]
            cycles.append(cycle)

    # Construct children
    child1 = [None]*18
    child2 = [None]*18
    for cycle in cycles:
        if (cycles.index(cycle) % 2 == 0):
            for column in cycle:
                child1[column[0]] = column[1]
                child2[column[0]] = column[2]
        else:
            for column in cycle:
                child1[column[0]] = column[2]
                child2[column[0]] = column[1]
    return child1, child2 

# Function that takes two lists and creates columns that contain the index value,
# and the value of the first and second list at that index (i.e. [3,4,5] and [6,7,8]
# create the columns [0,3,6], [1,4,7], and [2,5,8]). This is useful for cycle crossover.
def columnize(list1, list2):
    columns = []
    for node in list1:
        column = []
        index = list1.index(node)
        column.append(index)
        column.append(list1[index])
        column.append(list2[index])
        columns.append(column)
    return columns

# Function that selects parents from the population by roulette wheel (fitness proportionate)
# selection. !Incomplete!
def rouletteSelect():
    break

# Create nodes and edges (I intend to replace this with something
# more generic in the future)
normal = Node("Normal")
fire = Node("Fire")
water = Node("Water")
grass = Node("Grass")
electric = Node("Electric")
ice = Node("Ice")
fighting = Node("Fighting")
poison = Node("Poison")
ground = Node("Ground")
flying = Node("Flying")
psychic = Node("Psychic")
bug = Node("Bug")
rock = Node("Rock")
ghost = Node("Ghost")
dark = Node("Dark")
dragon = Node("Dragon")
steel = Node("Steel")
fairy = Node("Fairy")

fire.addOutgoing(grass)
fire.addOutgoing(ice)
fire.addOutgoing(bug)
fire.addOutgoing(steel)

water.addOutgoing(fire)
water.addOutgoing(ground)
water.addOutgoing(rock)

grass.addOutgoing(water)
grass.addOutgoing(ground)
grass.addOutgoing(rock)

electric.addOutgoing(water)
electric.addOutgoing(flying)

ice.addOutgoing(grass)
ice.addOutgoing(ground)
ice.addOutgoing(flying)
ice.addOutgoing(dragon)

fighting.addOutgoing(normal)
fighting.addOutgoing(ice)
fighting.addOutgoing(rock)
fighting.addOutgoing(dark)
fighting.addOutgoing(steel)

poison.addOutgoing(grass)
poison.addOutgoing(fairy)

ground.addOutgoing(fire)
ground.addOutgoing(electric)
ground.addOutgoing(poison)
ground.addOutgoing(rock)
ground.addOutgoing(steel)

flying.addOutgoing(grass)
flying.addOutgoing(fighting)
flying.addOutgoing(bug)

psychic.addOutgoing(fighting)
psychic.addOutgoing(poison)

bug.addOutgoing(grass)
bug.addOutgoing(psychic)
bug.addOutgoing(dark)

rock.addOutgoing(fire)
rock.addOutgoing(ice)
rock.addOutgoing(flying)
rock.addOutgoing(bug)

ghost.addOutgoing(psychic)
ghost.addOutgoing(ghost)

dragon.addOutgoing(dragon)

dark.addOutgoing(psychic)
dark.addOutgoing(ghost)

steel.addOutgoing(ice)
steel.addOutgoing(rock)
steel.addOutgoing(fairy)

fairy.addOutgoing(fighting)
fairy.addOutgoing(dragon)
fairy.addOutgoing(dark)

# Get a list of all nodes
nodes = []
for node in Node.instances:
    nodes.append(node)

#Initialization
population = []
for x in range(1, numPop + 1):
    copy = nodes.copy()
    random.shuffle(copy)
    individual = Chromosome(copy)
    population.append(individual)

# Testing
cycleCross(population[0], population[1])


    
    
    





