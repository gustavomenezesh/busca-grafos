class Graph:

  def __init__(self, filename):
    self.filename = filename
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

class DepthSearch:
  def __init__(self, graph, vert):
    self.t = 0
    self.graph = graph
    self.init()
    self.P(vert)
    self.generateGdf()

  def init(self):
    for i in range(self.graph.n):
      self.graph.depths.append([0,0,0])     #[PE, PS, PAI]

  def colorEdge(self, v, w, color):
    self.graph.colors[v-1][w-1][1] = color

  def P(self, v):
    self.t = self.t + 1
    self.graph.depths[v-1][0] = self.t
    for i in range(len(self.graph.adjacencyList[v-1])):
      w = self.graph.adjacencyList[v-1][i]
      if(self.graph.depths[w-1][0] == 0):
        self.colorEdge(v, w, '0,0,255')
        self.graph.depths[w-1][2] = v
        self.P(w)
      else:
        if(self.graph.depths[w-1][1] == 0 and w != self.graph.depths[v-1][2]):
          self.colorEdge(v, w, '255,0,0')
    self.t = self.t + 1
    self.graph.depths[v-1][1] = self.t

  def generateGdf(self):
    outputFile = self.graph.filename.split('.')[0] + '.gdf'
    with open(outputFile, 'w') as arquivo:
      arquivo.write('nodedef>name VARCHAR,label VARCHAR\n')
      for i in range(self.graph.n):
        arquivo.write(str(i+1)+','+str(i+1)+'\n')
      arquivo.write('edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n')
      for i in range(self.graph.n):
        for j in range(self.graph.n):
          if(self.graph.colors[i][j][0] and self.graph.colors[i][j][1] != '0,0,0'):
            arquivo.write(str(i+1)+","+str(j+1)+",false,'"+self.graph.colors[i][j][1]+"'\n")

graph = Graph('graph1.txt')
DepthSearch(graph, 1)