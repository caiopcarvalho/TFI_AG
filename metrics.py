import csv
import networkx as nx
import matplotlib.pyplot as plt

def _degree(G):
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
  
def coeficienteClusterizacao(G):
    clust_coeficiente =nx.clustering(G)
    nx.draw(G)
    plt.show()

g= nx.read_edgelist('users_friends.csv',delimiter=',',nodetype=int)
_degree(g)
print (nx.info(g))
print (g)
nx.draw(g)
plt.show()