from Graph import Graph
from Node import Node

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

graph = Graph()
graph.addNode(normal)
graph.addNode(fire)
graph.addNode(water)
graph.addNode(grass)
graph.addNode(electric)
graph.addNode(ice)
graph.addNode(fighting)
graph.addNode(poison)
graph.addNode(ground)
graph.addNode(flying)
graph.addNode(psychic)
graph.addNode(bug)
graph.addNode(rock)
graph.addNode(ghost)
graph.addNode(dragon)
graph.addNode(dark)
graph.addNode(steel)
graph.addNode(fairy)

print(graph.getCrosses())
