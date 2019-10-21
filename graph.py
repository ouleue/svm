class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
        self.distance=0
        self.pred=None
        self.color='white'
    def setColor(self,color):
        self.color=color
    def getColor(self):
        return self.color
    def setDistance(self,n):
        self.distance=n
    def getDistance(self):
        return self.distance
    def setPred(self,x):
        self.pred=x
    def getPred(self):
        return self.pred
    def addNeighbour(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    def __str__(self):
        return str(self.id)+' connectedTo: '+str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
    def addVertex(self,key):
        self.numVertices=self.numVertices+1
        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        return newVertex
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertList
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        self.vertList[f].addNeighbour(self.vertList[t],cost)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())

def buildGraph(wordFile):
    d={}
    g=Graph()
    wfile=open(wordFile,'r')
    for line in wfile:
        word=line[:-1]
        for i in range(len(word)):
            bucket=word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket]=[word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1,word2)
    return g

from pythonds.basic.queue import Queue
def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue=Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size()>0):
        currentVert=vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor()=='white'):
                nbr.setColor('grey')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    x=y
    while(x.getPred()):
        print (x.getId())
        x=x.getPred()
    print (x.getId())


wordgraph=buildGraph('fourletterwords.txt')
bfs(wordgraph,wordgraph.getVertex('FOOL'))
traverse(wordgraph.getVertex('SAGE'))




def knightGraph(bdSize):
    ktGraph=Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId=posToNodeId(row,col,bdSize)
            newPositions=genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid=posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid)
    return ktGraph

def posToNodeId(row,col,bdSize):
    return row*bdSize+col

def genLegalMoves(x,y,bdSize):
    newMoves=[]
    moveOffsets=[(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
    for i in moveOffsets:
        newX=x+i[0]
        newY=y+i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x>=0 and x<bdSize:
        return True
    else:
        return False

def knightTour(n,path,u,limit):
    u.setColor('grey')
    path.append(u)
    if n<limit:
        nbrList=list(u.getConnections())
        i=0
        done=False
        while i<len(nbrList) and not done:
            if nbrList[i].getColor()=='white':
                done=knightTour(n+1,path,nbrList[i],limit)
            i=i+1
        if not done:
            path.pop()
            u.setColor(white)
    else:
        done=True
    return done

def orderByAvail(n):
    resList=[]
    for v in n.getConnections():
        if v.getColor=='white':
            c=0
            for w in v.getConnections():
                if w.getColor=='white':
                    c=c+1
            resList.append((c,v))
    resList.sort(key=lambda x:x[0])
    return [y[1] for y in resList]

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time=0
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor()=='white':
                self.dfsvisit(aVertex)

def dfsvisit(self,startVertex):
    startVertex.setColor('gray')
    self.time+=1
    startVertex.setDiscovery(self.time)
    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor()=='white':
            nextVertex.setPred(startVertex)
            self.dfsvisit(nextVertex)
    startVertex.setColor('black')
    self.time+=1
    startVertex.setFinish(self.time)



















    