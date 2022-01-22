'''
1610 - Dudu Service Maker
Daniel Lessa
'''

class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []  

  def addNeighbor(self, node):
    self.neighbors.append(node)     

class Graph:
  def __init__(self, size):
    self.nodes = {}

    for x in range(1, size+1):
      self.nodes[x] = Node(x)

  def connect(self, first_value, second_value):
    first_nodes = self.nodes[first_value]
    second_nodes = self.nodes[second_value]
    first_nodes.addNeighbor(second_nodes)

  def moveNode(self, node, source_set, destination_set):
    source_set.remove(node)
    destination_set.add(node)    

  def depthFirstSearch(self, current, pendent_set, dependent_set, visited_set):
    self.moveNode(current, pendent_set, dependent_set)
    
    for neighbor in current.neighbors:
      if neighbor in dependent_set:
        return True
      elif neighbor in visited_set:
        continue
      elif self.depthFirstSearch(neighbor, pendent_set, dependent_set, visited_set):
        return True
    
    self.moveNode(current, dependent_set, visited_set)
    return False

  def foundCycle(self):
    pendent_set = set()
    dependent_set  = set()
    visited_set = set()

    for value in self.nodes.values():
      pendent_set.add(value)

    while len(pendent_set) > 0:
      # Utilizando um interável pra conseguir percorrer os nos próximos valores dos nós
      current = next(iter(pendent_set))
      
      if self.depthFirstSearch(current, pendent_set, dependent_set, visited_set):
        return True

    return False 

if __name__ == "__main__":
  t = int(input())
  
  for _ in range(t):
    n, m = map(int, input().split())
    graph = Graph(n)
    
    for _ in range(m):
      a, b = map(int, input().split())
      graph.connect(a, b)
      
    if (graph.foundCycle()):
      print("SIM")
    else:
      print("NAO")