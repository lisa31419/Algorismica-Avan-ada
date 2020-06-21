import networkx as nx
import matplotlib.pyplot as plt
import random as rd

plot = 0

# Genera un conjunto de objetos de prueba en forma de una lista de listas, 
# cada una de las cuales representa un elemento [peso,valor] o [peso,valor,cantidad]
def random_objects(infinite=True):
    elems = 10
    if infinite:
        return [[p,v] for p,v in zip(rd.sample(range(1, 50), k=elems), rd.sample(range(1, 100), k=elems))]
    else:
        return [[p,v,c] for p,v,c in zip(rd.sample(range(1, 50), k=elems), rd.sample(range(1, 100), k=elems),rd.sample(range(1, 15), k=elems))]

# Creates random graph (non-tree)
def random_graph(num_v = 15, num_e = 20):
    graph = nx.generators.gnm_random_graph(num_v,num_e)
    for edge in graph.edges():
        graph.add_edge(edge[0],edge[1],weight=round(rd.random(),3))
    return graph

# Show Graph
def draw_graph(G,size=7):
    global plot
    plt.figure(plot,(size,size))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G,with_labels=True,pos=pos)
    plot += 1

# Show Graph with highlighted path (path must be a list of edges)
def draw_path(G,path,size=7):
    global plot
    plt.figure(plot,(size,size))
    # Get distribution of graph elements
    pos = nx.spring_layout(G) 
    nx.draw_networkx(G,pos)
    # Get edges not in path
    other_edges = [e for e in G.edges() if e not in path]
    # Get weights for display
    labels_path = {edge:G.edges[edge[0],edge[1]]['weight'] for edge in path}
    labels_other = {edge:G.edges[edge[0],edge[1]]['weight'] for edge in other_edges}
    # Path in blue
    nx.draw_networkx_edges(G,pos,edgelist=path,edge_color='blue',width=5)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels_path,edgelist=path)
    # Rest of the edges in red
    nx.draw_networkx_edges(G,pos,edgelist=other_edges,edge_color='red')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels_other,edgelist=other_edges)
    # Increment plot counter
    plot += 1    