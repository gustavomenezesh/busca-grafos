class Graph:

  def __init__(self, filename):
    self.adjacencyMatrix = []
    self.adjacencyList = []
    self.depths = []
    self.colors = []
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

      for i in range(self.n):
        line = []
        for j in range(self.n):
          line.append([self.adjacencyMatrix[i][j], '0,0,0'])
        self.colors.append(line)

graph1 = Graph('graph2.txt')

t = 0
def init(graph):
  for i in range(graph.n):
    graph.depths.append([0,0,0])

def colorEdge(graph, v, w, color):
  graph.colors[v-1][w-1][1] = color

def P(graph, v):
  global t
  t = t + 1
  graph.depths[v-1][0] = t
  for i in range(len(graph.adjacencyList[v-1])):
    w = graph.adjacencyList[v-1][i]
    if(graph.depths[w-1][0] == 0):
      colorEdge(graph, v, w, '0,0,255')
      graph.depths[w-1][2] = v
      P(graph, w)
    else:
      if(graph.depths[w-1][1] == 0 and w != graph.depths[v-1][2]):
        colorEdge(graph, v, w, '255,0,0')
  t = t + 1
  graph.depths[v-1][1] = t

def generateGdf(graph):
  with open('graph2.gdf', 'w') as arquivo:
    arquivo.write('nodedef>name VARCHAR,label VARCHAR\n')
    for i in range(graph.n):
      arquivo.write(str(i+1)+','+str(i+1)+'\n')
    arquivo.write('edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n')
    for i in range(graph.n):
      for j in range(graph.n):
        if(graph.colors[i][j][0] and graph.colors[i][j][1] != '0,0,0'):
          arquivo.write(str(i+1)+","+str(j+1)+",false,'"+graph.colors[i][j][1]+"'\n")


init(graph1)
P(graph1, 1)
generateGdf(graph1)