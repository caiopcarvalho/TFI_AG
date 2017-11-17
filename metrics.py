import csv
import networkx as nx
import matplotlib.pyplot as plt

def degree(G):
    with open('degrees.csv', 'w') as f:
        writeit = csv.writer(f, delimiter=',')
        for node in G.nodes():
         writeit.writerow([str(node)] + [G.degree(node)])

def outDegree(G):
    with open('out_degrees.csv', 'w') as f:
        writeit = csv.writer(f, delimiter=',')
        for node in G.nodes():
         writeit.writerow([str(node)] + [G.out_degree(node)])

def inDegree(G):
    with open('in_degrees.csv', 'w') as f:
        writeit = csv.writer(f, delimiter=',')
        for node in G.nodes():
         writeit.writerow([str(node)] + [G.in_degree(node)])
  
def clusteringCoefficient(G):
    clust_coeficiente = nx.clustering(G)
    nx.draw(G)
    plt.show()

def bw_centrality(G):
    #G = nx.florentine_families_graph()
    bw_c = nx.betweenness_centrality(G, normalized=False)
    nx.draw(G)
    plt.show()

def edge_bw_centrality(G):
    bb = nx.edge_betweenness_centrality(G, normalized=False)
    nx.draw(G)
    plt.show()

def density(G):
    d = nx.density(G)
    nx.draw(G)
    plt.show()

g = nx.read_weighted_edgelist('rede2.csv',delimiter=',')    
#g= nx.read_edgelist('rede2.csv',delimiter=',',nodetype=int)
#_degree(g)
print (nx.info(g))
degree(G)
outDegree(G)
clusteringCoefficient(g)
inDegree(G)
bw_centrality(G)
edge_bw_centrality(G)
density(G)
