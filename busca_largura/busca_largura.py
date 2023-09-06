class Graph:

  def __init__(self, filename):
    self.filename = filename
    self.adjacencyMatrix = []
    self.adjacencyList = []
    self.fathers = []
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

class WidthSearch:
  def __init__(self, graph, vert):
    self.t = 0
    self.graph = graph
    self.queue = []
    self.checkeds = []
    self.init()
    self.run(vert)
    self.generateGdf()

  def init(self):
    for i in range(self.graph.n):
      self.graph.fathers.append(0)
      self.checkeds.append(0) #Desmarca todo mundo

  def colorEdge(self, v, w, color):
    self.graph.colors[v-1][w-1][1] = color

  def run(self, v):
    self.init()
    self.checkeds[v-1] = 1
    self.queue.append(v)
    while(len(self.queue)):
      for i in range(len(self.graph.adjacencyList[v-1])):
        w = self.graph.adjacencyList[v-1][i]
        if(self.checkeds[w - 1]):
          #visitar vw
          self.graph.fathers[w-1] = v
          self.checkeds[w-1] = 1
          self.queue.append(w)
        else:
          self.queue = self.queue[1:]

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
WidthSearch(graph, 1)