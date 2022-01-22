'''
1972 - Nêmesis
Daniel Lessa
'''

MAX_VALUE = 9999999

class Node:
  def __init__(self, value):
    if value == 'H' or value == 'E' or value == '.':
      self.value = 0
    elif value == '#':
      self.value = MAX_VALUE
    else:
      self.value = value
    
    self.partial_value = None
    self.origin = None
    self.neighbors = []               

  def addNeighbor(self, node):
    self.neighbors.append(node)     

  def setOrigin(self, origin):
    self.origin = origin

  def calculateReachedCost(self):
    if self.origin == None: 
      return MAX_VALUE
    elif self.origin == -1: 
      return 0
    else:
      return self.calculateCost() 

  def calculateCost(self):
    if self.origin == None:
      print('Valor invalido')
      return MAX_VALUE
    elif self.origin == -1:
      self.partial_value = 0
      return 0
    elif self.partial_value == None:
      self.partial_value = self.origin.calculateCost()
        
    return self.partial_value + self.value

class Graph:
  def __init__(self, n, m, values):
    self.m = m
    self.nodes = []

    for i in range(n):
      for j in range(m):
        self.nodes.append(Node(values[i][j]))

  def connect(self, first_value, second_value):
    first_nodes = self.nodes[first_value]
    second_nodes = self.nodes[second_value]
    
    if first_nodes.value == MAX_VALUE or second_nodes.value == MAX_VALUE:
      return
    
    first_nodes.addNeighbor(second_nodes)
    second_nodes.addNeighbor(first_nodes)

  def findBestPathCost(self, begin_i, begin_j, end_i, end_j):
    aux = []
    pile = []

    origin = self.nodes[begin_i*self.m+begin_j]
    origin.setOrigin(-1)
    pile.append(origin)
    aux.append(-1)
    
    while(len(pile) != 0):
      current = pile[0]
      
      for node in current.neighbors:
        index = 0

        if node.origin == None:
          node.setOrigin(current)
          cost = node.calculateCost()
          
          for i in range(len(aux)):
            if cost < aux[i]:
              break
            index = index + 1

          pile.insert(index, node) 
          aux.insert(index, cost)

        elif node.origin != -1:
          cost = node.calculateCost()
          cost_current = current.calculateCost() + node.value
          
          if cost > cost_current:
            node.setOrigin(current)
            pile.remove(node)
            aux.remove(cost)
            
            for i in range(len(aux)):
              if cost_current < aux[i]:
                break
              index = index + 1

            pile.insert(i, node) 
            aux.insert(i, cost_current)
            
      pile.remove(current)
      aux.remove(aux[0])

    return self.nodes[end_i*self.m+end_j].calculateReachedCost()

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
  if (final_cost >= MAX_VALUE):
    print('ARTSKJID')
  else:
    print(final_cost)
