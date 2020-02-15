# This project was created for the master's course MS549, Data Structures and Testing, and
# is called Project: Graph Application.  I have created a dataset of cities and distances (in miles) between them, and
# then applied that data to a graph using the python Networkx library (references shown throughout the code on
# all project pages).

# On this page, I created the basic code to pull the dataset information, add to it within the code, and then place
# it into the graph, in the format of: node (vector), node (vector), edge weights (distance)

# Reference when starting the project: https://www.youtube.com/watch?v=1ErL1z_lKd8&t=219s
# I created a txt file with nodes and edge data to pull from (DistanceDataSet.txt), but the nodes and edges can
# be created within the code also
# (reference: https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html)

import networkx as nx
import matplotlib.pyplot as plt

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
G.add_weighted_edges_from([('Los Angeles', 'Denver', 1016.1), ('Los Angeles', 'Phoenix', 373),
                           ('Phoenix', 'Nashville', 1636.1), ('Phoenix', 'New York', 2406.8),
                           ('Louisville', 'Albuquerque', 1301.4), ('Birmingham', 'Boston', 721.4),
                           ('Nashville', 'Louisville', 175.6), ('Milwaukee', 'Houston', 1172.2),
                           ('Phoenix', 'Birmingham', 1701.1), ('Los Angeles', 'Milwaukee', 2056.6),
                           ('Birmingham', 'Nashville', 191.6), ('Los Angeles', 'Toronto', 2518.8),
                           ('Pensacola', 'Toronto', 1203.8), ('New York', 'Las Vegas', 2252.5),
                           ('Denver', 'Boston', 1969.8), ('New York', 'Boston', 215.4),
                           ('Houston', 'Louisville', 950.8), ('Albuquerque', 'Topeka', 747.8),
                           ('Albuquerque', 'El Paso', 266.2), ('Las Vegas', 'El Paso', 730.7),
                           ('Tulsa', 'El Paso', 417.6), ('Las Vegas', 'Sioux Falls', 1370.6)])
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


nx.draw(G, with_labels=True, cmap=plt.get_cmap('viridis'), font_color='blue')
# reference for various layouts that can be chosen:
# https://networkx.github.io/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html
edge_labels = nx.draw_networkx_edge_labels(G, pos=nx.spectral_layout(G), font_size=7)
plt.suptitle('Distance Between Cities in Miles')
plt.get_figlabels()
plt.tight_layout(False)
plt.fill()
plt.figure(figsize=(300,300))
plt.show()

