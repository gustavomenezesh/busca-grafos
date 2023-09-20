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
    self.levels = []
    self.init()
    self.run(vert)
    self.generateGdf()

  def init(self):
    for i in range(self.graph.n):
      self.graph.fathers.append(0)
      self.checkeds.append(0) #Desmarca todo mundo
      self.levels.append(0)

  def colorEdge(self, v, w, color):
    self.graph.colors[v-1][w-1][1] = color

  def run(self, vert):
    self.init()
    self.checkeds[vert-1] = 1
    self.queue.append(vert)
    while(len(self.queue)):
      v = self.queue[0]
      for i in range(len(self.graph.adjacencyList[v-1])):
        w = self.graph.adjacencyList[v-1][i]
        if(self.checkeds[w - 1] == 0):
          self.colorEdge(v,w,'0,0,255')
          self.graph.fathers[w-1] = v
          self.checkeds[w-1] = 1
          self.levels[w-1] = self.levels[v-1] + 1
          self.queue.append(w)
        elif (self.levels[w-1] == self.levels[v-1]):
          if(self.graph.fathers[w-1] == self.graph.fathers[v-1]):
            self.colorEdge(v,w,'255,0,0')
          else:
            self.colorEdge(v,w,'255,255,0')
        elif(self.graph.fathers[w-1] == self.graph.fathers[v-1] + 1):
          self.colorEdge(v,w,'0,255,0')
      self.queue = self.queue[1:]
      print(self.queue)

  def generateGdf(self):
    outputFile = self.graph.filename.split('.')[0] + '_width.gdf'
    with open(outputFile, 'w') as arquivo:
      arquivo.write('nodedef>name VARCHAR,label VARCHAR\n')
      for i in range(self.graph.n):
        arquivo.write(str(i+1)+','+str(i+1)+'\n')
      arquivo.write('edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n')
      for i in range(self.graph.n):
        for j in range(self.graph.n):
          if(self.graph.colors[i][j][0] and self.graph.colors[i][j][1] != '0,0,0'):
            arquivo.write(str(i+1)+","+str(j+1)+",false,'"+self.graph.colors[i][j][1]+"'\n")

graph = Graph('teste.txt')
WidthSearch(graph, 1)