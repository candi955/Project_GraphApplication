

# Reference when starting the project: https://www.youtube.com/watch?v=1ErL1z_lKd8&t=219s
# I created a txt file with nodes and edge data to pull from (DistanceDataSet.txt), but the nodes and edges can
# be created within the code also
# (reference: https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html)

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

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


nx.draw(G, with_labels=True, cmap=plt.get_cmap('viridis'), font_color='white')
# reference for various layouts that can be chosen:
# https://networkx.github.io/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html
edge_labels = nx.draw_networkx_edge_labels(G, pos=nx.spectral_layout(G), font_size=5)
plt.suptitle('Distance Between Cities in Miles')
plt.get_figlabels()
plt.tight_layout(True)
plt.show()

