import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
import random



def ER(n, p):
    V = set([v for v in range(n)])
    E = set()
    for combination in combinations(V, 2):
        a = random.random()
        if a < p:
            E.add(combination)

    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)
    
    random.seed(10)
    rand_list = list(range(1, 63))
    random.shuffle(rand_list)
    for (u, v) in g.edges():
        i = random.randint(0,len(rand_list) - 1)
        g.edges[u,v]['weight'] = rand_list[i]
        i+=1

    return g

n = 150
p = 0.4
G = ER(n, p)
python_file = open("boruvka_input.txt", "w")
python_file.write(str(n)+'\n')
for node1, node2, data in G.edges(data=True):
    data = str(node1) + ' '+ str(node2) + ' ' + str(data['weight']) + '\n'
    python_file.write(data)

python_file.close()

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.title("Random Graph Generation Example")
plt.show()

