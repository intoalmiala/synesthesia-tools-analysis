import sys
import json
import numpy as np


# Command line arguments: input files
INPUT_FILE_1 = sys.argv[1]
INPUT_FILE_2 = sys.argv[2]


# Define input sets as the colors from the specified files
with open(INPUT_FILE_1) as f:
    set1 = [tuple(y) for x in json.load(f).values() for y in x]

with open(INPUT_FILE_2) as f:
    set2 = [tuple(y) for x in json.load(f).values() for y in x]


# Define number of voxels and initialize distributions in each voxel
n = 2
f = np.zeros(n**3)
g = np.zeros(n**3)

# Count distributions in voxels
for color in set1:
    x = int(round(color[0]/255))
    y = int(round(color[1]/255))
    z = int(round(color[2]/255))
    f[n**2 * x + n * y + z] += 1/len(set1)

for color in set2:
    x = int(round(color[0]/255))
    y = int(round(color[1]/255))
    z = int(round(color[2]/255))
    g[n**2 * x + n * y + z] += 1/len(set2)


# Calculate L1 distance between the distributions
distance = sum([abs(x - y) for (x, y) in zip(f, g)])

print(distance)
