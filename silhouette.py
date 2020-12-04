import sys
import json
from functools import reduce

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt


# Command line arguments
INPUT_FILE = sys.argv[1]
MAX_N_CLUSTERS = int(sys.argv[2]) if len(sys.argv) > 2 else 10


# Read data from input file
with open(INPUT_FILE) as f:
    X = np.array(reduce(lambda x, y: x+y, json.load(f).values(), []))


# Calculate clusters using k-means and decide cluster amount using silhouette
scores = []
kmeans = []
for i in range(MAX_N_CLUSTERS-1):
    n_clusters = i + 2
    kmeans.append(KMeans(n_clusters = n_clusters))
    prediction = kmeans[i].fit_predict(X)
    scores.append(silhouette_score(X, prediction))
    print(f"For {n_clusters} clusters got a score of {scores[n_clusters]}.")

best_score = 0
best_i = 0
for i, score in enumerate(scores):
    if score > best_score:
        best_score = score
        best_i = i

print(f"Best cluster amount was {best_i + 2} with a score of {best_score}.")

model = kmeans[best_i]


# Plot clusters
fig = plt.figure()
cluster_colors = kmeans.cluster_centers_/255

# For plotting only cluster colors #
ax = plt.axes(projection = "3d")
ax.scatter(X[:,0], X[:,1], X[:,2], c = cluster_colors[kmeans.labels_])
# -------------------------------- #

# For plotting cluster colors and true colors side by side #
#ax1 = fig.add_subplot(1, 2, 1, projection = "3d")
#ax1.scatter(X[:,0], X[:,1], X[:,2], c = cluster_colors[kmeans.labels_])
#
#colors = np.array([tuple(map(lambda x: x/255, X[i])) for i in range(len(X))])
#ax2 = fig.add_subplot(1, 2, 2, projection = "3d")
#ax2.scatter(X[:,0], X[:,1], X[:,2], c = colors)
# -------------------------------------------------------- #

plt.show()
