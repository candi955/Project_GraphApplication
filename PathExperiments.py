

# Reference when starting the project: https://www.youtube.com/watch?v=1ErL1z_lKd8&t=219s
# I created a txt file with nodes and edge data to pull from (DistanceDataSet.txt), but the nodes and edges can
# be created within the code also
# (reference: https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html)

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from scipy.cluster import hierarchy
from scipy.spatial import distance

# Using the color class in python, in assigned variable form, to make the headings bold, underline, and various colors
# (colorama module), reference: https://pypi.org/project/colorama/,
# and package colors, reference: https://godoc.org/github.com/whitedevops/colors
# reference: https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
endColor = "\033[0m"

startBold = "\033[1m"
startUnderline = '\033[4m'
startDarkCyan = '\033[36m'
startPurple = '\033[95m'
startCyan = '\033[96m'
startBlue = '\033[94m'
startGreen = '\033[92m'
startYellow = '\033[93m'
startRed = '\033[91m'
startBlack = "\033[30m"

BackgroundMagenta = "\033[45m"

# Creating a background in the color magenta
print(BackgroundMagenta)

# references: https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.readwrite.edgelist.read_weighted_edgelist.html
# https://stackoverflow.com/questions/43440478/error-using-networkx-weighted-edgelist

# Pulling node and edge information from the txt file and assigning the information to variable G
# reference: https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.readwrite.edgelist.read_weighted_edgelist.html
# https://stackoverflow.com/questions/43440478/error-using-networkx-weighted-edgelist
G = nx.read_weighted_edgelist('DistanceDataSet.txt')
# Placing the dataset general information as output
print(startBlack + '\nDataset information when pulled from the DistanceDataSet.txt file:\n', nx.info(G))

# Side note: to convert graph to undirected graph for certain measurements if needed:
#  H = nx.Graph(G) # convert G to undirected graph
# reference: https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html

# Adding more nodes and weights to the dataset variable G
# reference: https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
G.add_weighted_edges_from([('Los Angeles', 'Nashville', 2003.8), ('Los Angeles', 'Phoenix', 373),
                           ('Phoenix', 'Nashville', 1636.1), ('Phoenix', 'Toronto', 2213.9),
                           ('Pensacola', 'Los Angeles', 2069.3), ('Birmingham', 'Los Angeles', 2036.5),
                           ('Nashville', 'Milwaukee', 328.9), ('Milwaukee', 'Pensacola', 1008.9),
                           ('Phoenix', 'Birmingham', 1701.1), ('Los Angeles', 'Milwaukee', 2056.6),
                           ('Birmingham', 'Nashville', 191.6), ('Los Angeles', 'Toronto', 2518.8),
                           ('Pensacola', 'Toronto', 1203.8), ('Birmingham', 'Milwaukee', 758)])
# Placing the updated dataset information as output
print('\nDataset information after adding more node and distance sets:\n', nx.info(G))

# Ending the color magenta as background
print(endColor)

print(startBlue + '\nNumber of nodes:' + endColor, nx.number_of_nodes(G))
print(startBlue + '\nNumber of edges:' + endColor, nx.number_of_edges(G))
# Basically, for directed, does direction matter in the graph?
# Otherwise, for undirected, can the node pairs go in either direction?
# reference: https://stackoverflow.com/questions/23956467/what-is-the-difference-between-a-directed-and-undirected-graph
print(startBlue + '\nIs the graph directed?' + endColor, nx.is_directed(G))


# reference for below weighted graph code:
# https://networkx.github.io/documentation/networkx-1.10/examples/drawing/weighted_graph.html
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] >0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <=0.5]

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2)
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=2, alpha=0.5, edge_color='b', style='dashed')

# labels
nx.draw_networkx_labels(G, pos, font_size=11, font_family='sans-serif', font_color='blue')
nx.draw_networkx_edge_labels(G, pos=nx.spectral_layout(G), font_size=5)

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.tight_layout(True)
plt.suptitle('Original Distance Model (miles)')
plt.show() # display





print(startPurple + '\n----------------------------------------- Algorithmic Path Experiments with Data, Original '
                      'Graph -----------------------------------------' + endColor, '\n')

print(startBlue + '\nShortest path from Pensacola to Phoenix:\n'+ endColor, nx.shortest_path(G, 'Pensacola', 'Phoenix'))
print(startBlue + '\nDijkstra path from Pensacola to Phoenix:\n'+ endColor, nx.dijkstra_path(G, 'Pensacola', 'Phoenix'))
# Eulerian:
# reference: https://networkx.github.io/documentation/stable/reference/algorithms/euler.html
# For Use-Case scenerio, see Eulerian Graph at bottom of program
print(startBlue + '\nHas Eulerian path:\n'+ endColor, nx.has_eulerian_path(G))
print(startBlue + '\nIs semi-Eulerian:\n'+ endColor, nx.is_semieulerian(G))
# Shortest paths (Bellman Ford):
# reference: https://networkx.github.io/documentation/stable/reference/algorithms/shortest_paths.html
# defined: The Bellman-Ford algorithm is a graph search algorithm that finds the shortest path between a given source
# vertex and all other vertices in the graph. This algorithm can be used on both weighted and unweighted graphs.
# reference: https://brilliant.org/wiki/bellman-ford-algorithm/
print(startBlue + '\nBellman Ford path from Los Angeles:\n'+ endColor,
      nx.bellman_ford_predecessor_and_distance(G, 'Los Angeles'))
# Linear Algebra (Eigenvalues):
# reference: https://networkx.github.io/documentation/stable/reference/linalg.html
# defined: Using scaler multiplication (matrix multiplication = scaler multiplication) to create a new figure,
# utilizing Eigenvalues and Eigenvectors
# reference: https://www.youtube.com/watch?v=vs2sRvSzA3o
# Real world use-case: To scale a model to a real-world dataset or graph
# Reference: http://barabasi.com/f/94.pdf
print(startBlue + '\nThe Modularity Spectrum that returns eigenvalues of the modularity matrix of G:\n' +
      endColor, nx.modularity_spectrum(G))




print(startCyan + '\n----------------------------------------- Transforming Graph into Eulerian Graph' +
      '-----------------------------------------' + endColor, '\n')
# reference: https://networkx.github.io/documentation/stable/reference/algorithms/euler.html
# Use-Case example: The purpose of the proposed new roads is to make the town mailman-friendly. In graph theory terms,
# we want to change the graph so it contains an Euler circuit. This is also referred to as Eulerizing a graph. The
# most mailman-friendly graph is the one with an Euler circuit since it takes the mailman back to the starting point.
# This means that the mailman can leave his car at one intersection, walk the route hitting all the streets just once,
# and end up where he began. There is no backtracking or walking of streets twice. This saves him time.
# reference: https://study.com/academy/lesson/eulerizing-graphs-in-math.html

# reference for below weighted graph code:
# https://networkx.github.io/documentation/networkx-1.10/examples/drawing/weighted_graph.html
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] >0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <=0.5]

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2)
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=2, alpha=0.5, edge_color='b', style='dashed')

# labels
nx.draw_networkx_labels(G, pos, font_size=11, font_family='sans-serif', font_color='blue')
nx.draw_networkx_edge_labels(G, pos=nx.spectral_layout(G), font_size=5)

nx.eulerize(G)

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.tight_layout(True)
plt.suptitle('Eulerized Graph, Distance Model (miles)')
plt.show() # display

print(startGreen + '-------------                           Algorithmic Path Experiments post-Eulerian Graph' +
      '                      -------------' + endColor, '\n')

print(startBlue + '\nShortest path from Pensacola to Phoenix, Eulerized Graph:\n'+ endColor,
      nx.shortest_path(G, 'Pensacola', 'Phoenix'))
print(startBlue + '\nDijkstra path from Pensacola to Phoenix, Eulerized Graph:\n'+ endColor,
      nx.dijkstra_path(G, 'Pensacola', 'Phoenix'))



