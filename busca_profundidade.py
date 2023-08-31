class Graph:

  def __init__(self, filename):
    self.adjacencyMatrix = []
    self.adjacencyList = []
    self.depths = []
    with open(filename, 'r') as file:
      self.n = int(file.readline().strip())

      for _ in range(self.n):
        line = file.readline().strip()
        items = line.split()
        lineMatrix = [int(item) for item in items]
        self.adjacencyMatrix.append(lineMatrix)

      for i in range(self.n):
        neighbors = []
        for j in range(self.n):
          if(self.adjacencyMatrix[i][j] == 1):
            neighbors.append(j + 1)
        self.adjacencyList.append(neighbors)

graph1 = Graph('graph2.txt')

t = 0
def init(graph):
  for i in range(graph.n):
    graph.depths.append([0,0,0])

def P(graph, v):
  global t
  t = t + 1
  graph.depths[v-1][0] = t
  for i in range(len(graph.adjacencyList[v-1])):
    w = graph.adjacencyList[v-1][i]
    if(graph.depths[w-1][0] == 0):
      #visitar aresta vw azul
      print('azul')
      graph.depths[w-1][2] = v
      P(graph, w)
    else:
      if(graph.depths[w-1][1] == 0 and w != graph.depths[v-1][2]):
        # visitar aresta vw vermelha
        print('vermelha')
  t = t + 1
  graph.depths[v-1][1] = t

init(graph1)
P(graph1, 1)
print(graph1.depths)
