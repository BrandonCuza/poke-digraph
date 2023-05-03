from Chromosome import Chromosome
from Node import Node
import random

numPop = 1000
numGen = 1000

# Function that takes two parents and returns two children created through
# cycle crossover. !Incomplete!
def cycleCross(parent1, parent2):
    cycles = []
    p1 = parent1.getNodes().copy()
    for node in p1:
        print(node.getName())
    print("\n")
    p2 = parent2.getNodes().copy()
    for node in p2:
        print(node.getName())
    print("\n")
    while True:
        cycle = []
        i = 0
        cycle.append(p1.pop(i))
        while True:
            nextNum = p2[i]
            try:
                temp = p1.index(nextNum)
                cycle.append(p2.pop(i))
                i = temp
                p1.pop(i)
            except ValueError:
                p2.pop(i)
                cycles.append(cycle)
                break
        if len(p1) == 0:
            break
    for cycle in cycles:
        for node in cycle:
            print(node.getName())
        print("\n")
                
            
        
        

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


    
    
    





