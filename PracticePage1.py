

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
G.add_weighted_edges_from([('Los Angeles', 'Nashville', 2003.8), ('Los Angeles', 'Phoenix', 373)])
# Placing the updated dataset information as output
print('\nDataset information after adding two node and distance sets:\n', nx.info(G))

# Ending the color magenta as background
print(endColor)


