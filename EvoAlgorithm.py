from Chromosome import Chromosome
from Node import Node
import random

popSize = 100 #Population size
numGen = 1000 #Number of generations
crossoverProb = 0.5 #Probability of crossover occuring
mutationProb = .05 #Probability of mutation occuring

"""
 Function that takes two parents and returns two children created through
 cycle crossover.
"""
def cycleCrossover(parents):
    
    r = random.random()
    if r < crossoverProb:
        
        parent1 = parents[0].getNodes()
        parent2 = parents[1].getNodes()

        columns = columnize(parent1, parent2)

        cycles = []
        for column in columns:

            # Check if the column is already in a cycle
            new = True
            for cycle in cycles:
                if column in cycle:
                    new = False

            # If not, it is the head of a new cycle     
            if new:
                head = column[1]
                nextVert = column[2]
                cycle = [column]
                
                # Find columns in this cycle, end when the next vertex is the same as the head
                while nextVert != head:
                    for otherColumn in columns:
                        if otherColumn[1] == nextVert:
                            cycle.append(otherColumn)
                            nextVert = otherColumn[2]
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
        child1 = Chromosome(child1)
        child2 = Chromosome(child2)
        children = [child1, child2]

        return children
    
    else:
        return parents

"""  
 Function that takes two lists and creates columns that contain the index value,
 and the value of the first and second list at that index (i.e. [3,4,5] and [6,7,8]
 create the columns [0,3,6], [1,4,7], and [2,5,8]). This is useful for cycle crossover.
"""
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

"""
 Function that selects parents from the population by roulette wheel (fitness proportionate)
 selection.
"""
def rouletteSelect(population):

    populationCopy = population.copy()
    parents = []

    # Get cumulative fitness of the population
    totalFitness = 0
    for individual in populationCopy:
        totalFitness += individual.getFitness()

    # Cycle through the population until 2 parents are chosen by roulette wheel selection
    numChosen = 0
    while numChosen < 2:
        index = 0
        cumulativeChance = 0.0
        r = random.random()
        while (cumulativeChance <= r):
            
            # Because of float impercision cumulative chance doesn't reach exactly 1.00, and sometimes the
            # random number generator chooses a value slightly higher than cumulative chance can reach. This
            # try-except block chooses the last individual in the population if that happens.
            try:
                testee = populationCopy[index]
            except IndexError:
                parents.append(populationCopy.pop(-1))
                numChosen +=1
                break
            
            testeeFitness = testee.getFitness()
            cumulativeChance += testeeFitness/totalFitness
            if (r < cumulativeChance):
                parents.append(populationCopy.pop(index))
                numChosen += 1
            else:
                index += 1

    return parents

"""
 Function that mutates a given individual by swapping two random nodes with each other
"""
def swapMutate(chromosome):
    r = random.random()
    if r < mutationProb:
        nodes = chromosome.getNodes()
        limit = len(nodes)
        index1 = random.randint(0,limit-1)
        index2 = random.randint(0,limit-1)
        if index1 != index2:
            temp = nodes[index1]
            nodes[index1] = nodes[index2]
            nodes[index2] = temp
        chromosome.updateFitness()
        return
    
    else:
        return

###################################################################################################################
###################################################################################################################

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
for x in range(1, popSize + 1):
    copy = nodes.copy()
    random.shuffle(copy)
    individual = Chromosome(copy)
    population.append(individual)

# Testing

for x in range (1, numGen + 1):
    newPop = []
    for y in range (1, (popSize//2) + 1):
        parents = rouletteSelect(population)
        children = cycleCrossover(parents)
        for individual in children:
            swapMutate(individual)
            newPop.append(individual)
    population = newPop

bestInd = None
bestFit = -1
for individual in population:
    if individual.getFitness() > bestFit:
        bestFit = individual.getFitness()
        bestInd = individual
print("Lowest Crosses Found: " + str(-(bestFit - 400)))
for node in bestInd.getNodes():
    print(node.getName())
    
    
    





