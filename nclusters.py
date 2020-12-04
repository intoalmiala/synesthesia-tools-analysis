import json
import sys
from functools import reduce
import numpy as np
from sklearn.cluster import KMeans

# Command line arguments
INPUT_FILE = sys.argv[1]
N_CLUSTERS = int(sys.argv[2])


# Read data from input file
with open(INPUT_FILE) as f:
    X = np.array(reduce(lambda x, y: x+y, json.load(f).values(), []))


# Calculate clusters using k-means
kmeans = KMeans(n_clusters = N_CLUSTERS)
kmeans.fit(X)


# Plot clusters
import matplotlib.pyplot as plt

cluster_colors = kmeans.cluster_centers_/255

fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.scatter(X[:,0], X[:,1], X[:,2], c = cluster_colors[kmeans.labels_])

plt.show()
