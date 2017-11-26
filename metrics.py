import csv
import networkx as nx
from networkx import NetworkXError
import matplotlib.pyplot as plt
from collections import Counter
import sys

#Grau médio
def degree(G):
    with open('degrees.csv', 'w',newline='') as f:
        writeit = csv.writer(f, delimiter=',')
        for node in G.nodes():
         writeit.writerow([G.degree(node)]+[str(node)])

def outDegree(G):
    with open('out_degrees.csv', 'w',newline='') as f:
        writeit = csv.writer(f, delimiter=',')
        for node in G.nodes():
         writeit.writerow([G.out_degree(node)]+[str(node)])

def inDegree(G):
    with open('in_degrees.csv', 'w',newline='') as f:
        writeit = csv.writer(f, delimiter=',')
        for node in G.nodes():
         writeit.writerow([G.in_degree(node)]+[str(node)])

def writeFile (nodo,cluster):
    with open('clustering.csv', 'a') as f:
	    writeit = csv.writer(f, delimiter=',', lineterminator='\n')
	    writeit.writerow(nodo+cluster)

#Método que salva coeficiente de clustering em um arquivo csv   
def clustering(G,nodes=None,weight=None):
    if G.is_directed():
        raise NetworkXError('Clustering algorithms are not defined ',
                            'for directed graphs.')
    if weight is not None:
        td_iter=_weighted_triangles_and_degree_iter(G,nodes,weight)
    else:
        td_iter=_triangles_and_degree_iter(G,nodes)

    clusterc={}

    for v,d,t in td_iter:
        if t==0:
            clusterc[v]=0.0
        else:
            clusterc[v]=t/float(d*(d-1))
            writeFile([v],[str(t/float(d*(d-1)))])


    #if nodes in G: 
        #return list(clusterc.values())[0] # return single value
    #return clusterc

def _weighted_triangles_and_degree_iter(G, nodes=None, weight='weight'):
    """ Return an iterator of (node, degree, weighted_triangles).  
    
    Used for weighted clustering.

    """
    if G.is_multigraph():
        raise NetworkXError("Not defined for multigraphs.")

    if weight is None or G.edges()==[]:
        max_weight=1.0
    else:
        max_weight=float(max(d.get(weight,1.0) 
                             for u,v,d in G.edges(data=True)))
    if nodes is None:
        nodes_nbrs = G.adj.items()
    else:
        nodes_nbrs= ( (n,G[n]) for n in G.nbunch_iter(nodes) )

    for i,nbrs in nodes_nbrs:
        inbrs=set(nbrs)-set([i])
        weighted_triangles=0.0
        seen=set()
        for j in inbrs:
            wij=G[i][j].get(weight,1.0)/max_weight
            seen.add(j)
            jnbrs=set(G[j])-seen # this keeps from double counting
            for k in inbrs&jnbrs:
                wjk=G[j][k].get(weight,1.0)/max_weight
                wki=G[i][k].get(weight,1.0)/max_weight
                weighted_triangles+=(wij*wjk*wki)**(1.0/3.0)
        yield (i,len(inbrs),weighted_triangles*2)

def _triangles_and_degree_iter(G,nodes=None):
    """ Return an iterator of (node, degree, triangles).  

    This double counts triangles so you may want to divide by 2.
    See degree() and triangles() for definitions and details.

    """
    if G.is_multigraph():
        raise NetworkXError("Not defined for multigraphs.")

    if nodes is None:
        nodes_nbrs = G.adj.items()
    else:
        nodes_nbrs= ( (n,G[n]) for n in G.nbunch_iter(nodes) )

    for v,v_nbrs in nodes_nbrs:
        vs=set(v_nbrs)-set([v])
        ntriangles=0
        for w in vs:
            ws=set(G[w])-set([w])
            ntriangles+=len(vs.intersection(ws))
        yield (v,len(vs),ntriangles)

#Betweennes nodos
def bw_centrality(G):
    bw_c = nx.betweenness_centrality(G, normalized=False)
    print(bw_c)
    
#Betweennes arestas  
def edge_bw_centrality(G):
    bb = nx.edge_betweenness_centrality(G, normalized=False)
    print(bb)

#Método que mostra Coeficiente de Clustering no console
def clusteringCoefficient (G):
    cc=nx.clustering(G)
    print(cc)
    
#Distância média
def closenessCentrality(G):
    cc=nx.closeness_centrality(G)
    print(cc)

#Plota coeficiente de Clustering
def plotClustering():
    with open('clustering.csv','r') as inf:
        x = []
        y = []
        data = csv.reader(inf, delimiter=',')
        for line in data:
         tx, ty = line
         x.append((tx))
         #lendo apenas as 4 primeiras strings
         y.append((ty[0:6]))

    c = Counter(y)
    y1 = c.keys()
    x1 = c.values()
    fig = plt.figure()
    plt.title('Coeficiente de Clustering')
    plt.xlabel('Values')
    plt.ylabel('Count')
    plt.plot(x1,y1,'ro',color='red')
    fig.savefig('plotClustering.pdf')
    sys.exit(0)

#Plota  Degree, out Degree e in Degree
def plotDegrees(file):
    with open(file,'r') as inf:
        x = []
        y = []
        data = csv.reader(inf, delimiter=',')
        for line in data:
         tx = line[0]
         x.append((tx))

    c = Counter(x)
    y1 = c.values()
    x1 = c.keys()
    fig = plt.figure()
    plt.title('xxxxx')
    plt.xlabel("Values")
    plt.ylabel('Count')
    plt.plot(x1,y1,'ro',color='black')
    plt.show()
    #fig.savefig('Out_Degree.pdf')
    sys.exit(0)

g = nx.read_weighted_edgelist('grafo.csv',delimiter=',')
g1 = nx.read_edgelist('grafo.csv',delimiter=',',nodetype=int)
g1 = g1.to_directed()
print (nx.info(g1))
#clusteringCoefficient(g)
degree(g)
inDegree(g1)
outDegree(g1)
closenessCentrality(g)
clustering(g)
bw_centrality(g)
edge_bw_centrality(g)
plotDegrees('degrees.csv')
plotDegrees('out_degrees.csv')
plotDegrees('in_degrees.csv')
plotClustering()

