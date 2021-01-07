import sys
import json
import numpy as np


# Command line arguments: input files
# First argument is the file containing all of the data
# Second argument is a file containinga a subset of the data
INPUT_FILE_1 = sys.argv[1]
INPUT_FILE_2 = sys.argv[2]

with open(INPUT_FILE_1) as f:
    A = json.load(f).values()

with open(INPUT_FILE_2) as f:
    B = json.load(f).values()


# Plotting
import matplotlib.pyplot as plt

X = np.array([y for x in A for y in x])
Y = np.array([y for x in B for y in x])

A = np.zeros(8)
for i, color in enumerate(X):
    r = round(color[0]/255)
    g = round(color[1]/255)
    b = round(color[2]/255)
    A[4*r + 2*g + b] += 1/len(X)

B = np.zeros(8)
for i, color in enumerate(Y):
    r = round(color[0]/255)
    g = round(color[1]/255)
    b = round(color[2]/255)
    B[4*r + 2*g + b] += 1/len(Y)

color_names = ["musta", "sininen", "vihreä", "syaani", "punainen", "magenta", "keltainen", "valkoinen"]
colors = ["black", "blue", "lime", "cyan", "red", "magenta", "yellow", "white"]
ylims = [-0.5, 0.5]

fig, ax = plt.subplots()
ax.bar(range(len(A)), B-A, color=colors, tick_label=color_names, edgecolor="black")
ax.set_title(input("Title for difference plot: "))
ax.set_ylim(ylims)
ax.axhline(0, color="black", linewidth=1)
ax.tick_params(labelrotation=30)
plt.show()

fig, bx = plt.subplots()

bx.bar(range(len(A)), A, color=colors, tick_label=color_names, edgecolor="black")
bx.set_title(input("Title for plot of all data: "))
bx.set_ylim(ylims)
bx.axhline(0, color="black", linewidth=1)
bx.tick_params(labelrotation=30)
plt.show()

fig, cx = plt.subplots()
cx.bar(range(len(B)), B, color=colors, tick_label=color_names, edgecolor="black")
cx.set_title(input("Title for plot of subset of data: "))
cx.set_ylim(ylims)
cx.axhline(0, color="black", linewidth=1)
cx.tick_params(labelrotation=30)

plt.show()
