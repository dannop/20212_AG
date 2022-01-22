'''
1972 - Nêmesis
Daniel Lessa
'''

from cmath import inf

class Node:
  def __init__(self, value):
    if value == 'H' or value == 'E' or value == '.':
      self.value = 0
    elif value == '#':
      self.value = inf
    else:
      self.value = int(value)
    
    self.origin = None
    self.name = value
    self.neighbors = []  

  def addNeighbor(self, node):
    self.neighbors.append(node)     

  def setOrigin(self, origin):
    self.origin = origin

  def calculateCost(self):
    if self.origin == None or self.origin == -1: 
      return self.value
    else:
      return self.origin.calculateCost() + self.value

class Graph:
  def __init__(self, n, m, values):
    self.n = n
    self.m = m
    self.nodes = {}

    for i in range(n):
      for j in range(m):
        self.nodes[i*m+j] = Node(values[i][j])

  def connect(self, first_value, second_value):
    first_nodes = self.nodes[first_value]
    second_nodes = self.nodes[second_value]
    first_nodes.addNeighbor(second_nodes)
    second_nodes.addNeighbor(first_nodes)

  def findBestPathCost(self, begin_i, begin_j, end_i, end_j):
    pile = []
    origin = self.nodes[begin_i*self.m+begin_j]
    origin.setOrigin(-1)
    pile.append(origin)
    
    while(len(pile) != 0):
      current = pile[0]
      for node in current.neighbors:
        if node.origin == None:
          node.setOrigin(current)
          pile.append(node)
        else:
          if node.calculateCost() > current.calculateCost() + node.value:
            node.setOrigin(current)
            pile.append(node)
      pile.remove(current)

    return self.nodes[end_i*self.m+end_j].calculateCost()

if __name__ == "__main__":
  maze = []
  n, m = map(int, input().split(" "))
  h = []
  e = []
  
  for i in range(n):
    input_line = input()
    line = []
    
    for c in input_line: 
      line.append(c)
      if c == 'H':
        h.append(i)
        h.append(len(line)-1)
      elif c == 'E':
        e.append(i)
        e.append(len(line)-1)

    maze.append(line)

  graph = Graph(n, m, maze)

  for i in range(n):
    for j in range(m-1):
      graph.connect(i*m+j, i*m+(j+1))

  for j in range(m):
    for i in range(n-1):
      graph.connect(i*m+j, (i+1)*m+j)
  
  final_cost = graph.findBestPathCost(h[0], h[1], e[0], e[1])
  if (final_cost == inf):
    print('ARTSKJID')
  else:
    print(final_cost)
