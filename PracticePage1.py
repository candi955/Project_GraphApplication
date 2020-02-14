

# Reference when starting the project: https://www.youtube.com/watch?v=1ErL1z_lKd8&t=219s
# I created a txt file with nodes and edge data to pull from (DistanceDataSet.txt), but the nodes and edges can
# be created within the code also
# (reference: https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html)

import networkx as nx
import matplotlib.pyplot as plt

# references: https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.readwrite.edgelist.read_weighted_edgelist.html
# https://stackoverflow.com/questions/43440478/error-using-networkx-weighted-edgelist

G = nx.read_weighted_edgelist('DistanceDataSet.txt')
print(nx.info(G))