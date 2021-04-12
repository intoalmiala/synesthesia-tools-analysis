# Analysis

## Overview
This directory contains 6 programs:
* `chi-square.py`: calculates the [chi square goodness of fit test](https://en.wikipedia.org/wiki/Chi-squared_test) on given datasets
* `k-means.py`:  divides the given data points into a given amount of clusters using the [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) algorithm
* `silhouette.py`: calculates the optimal number of clusters for [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) for the given dataset using the [silhouette algorithm](https://en.wikipedia.org/wiki/Silhouette_(clustering))
* `plotter.py`: generates the following plots from the two given datasets: distribution of colors in both sets and the difference in those distributions
* `color-distribution-distance.py`: calculates the color distribution distance between the two given datasets

### Requirements
[Python 3](https://www.python.org/) is required by all of the programs. It is assumed that the user has access to a [Unix shell](https://en.wikipedia.org/wiki/Unix_shell) or can run and give command line arguments to Python programs by other means. Some additional third-party libraries are also required by some of the programs. Details are provided in each program's own subsection.

All of the third party libraries needed to use all programs are the following:
* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)
* [scikit-learn](https://scikit-learn.org/stable/index.html)

---

## Programs
The following sections will describe the requirements, usage, and functionality of these programs.

### chi-square.py
Calculates the chi-square value of the given subset compared to the other given dataset.

#### Requirements
* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/) if one wishes to plot the data in a 3d plot


#### Usage
    $ python3 chi-square.py SUBSET DATA
where `SUBSET` is a path to a JSON file containing data of a certain subset of the whole data, and `DATA` is a path to a JSON file containing the whole data (to which the subset is compared to).


#### How it works
The chi-square algorithm is described on [this Wikipedia page](https://en.wikipedia.org/wiki/Goodness_of_fit#Pearson's_chi-squared_test). In the case of our study, we divided the RGB-colorspace into 8 smaller congruent cubes, each corresponding to a studied color (i.e. a 3-bit color). The number of cubes can be changed by changing the variable `n` in the code: the cube will be divided into `n`³ cubes.

---

### k-means.py
Divides the data into a given amount of clusters using the [k-means clustering algorithm](https://en.wikipedia.org/wiki/K-means_clustering).

#### Requirements
* [numpy](https://numpy.org/)
* [scikit-learn](https://scikit-learn.org/stable/index.html)
* [matplotlib](https://matplotlib.org/)


#### Usage
    $ python3 k-means.py DATA N
where `DATA` is the path to a JSON file containing the dataset, and `N` is the cluster amount.


#### How it works
The program uses scikit-learn's k-means algorithm to cluster the data and then plots it using matplotlib.

---

### silhouette.py
Calculates the optimal number of clusters to divide the data to using the [silhouette algorithm](https://en.wikipedia.org/wiki/Silhouette_(clustering)) and divides the data into that many clusters using the [k-means algorithm](https://en.wikipedia.org/wiki/K-means_clustering).

#### Requirements
* [numpy](https://numpy.org/)
* [scikit-learn](https://scikit-learn.org/stable/index.html)
* [matplotlib](https://matplotlib.org/)


#### Usage
    $ python3 silhouette.py DATA N
where `DATA` is the path to a JSON file containing the dataset, and `N` is the maximum cluster amount to be tested.


#### How it works
For each cluster amount from 2 to the given maximum cluster count the silhouette score is calculated and the scores logged. Then the cluster count with the best score logged and the k-means clustering plotted in a 3d plot.

---

### plotter.py
Plots three plots: color distributions in the two given datasets and the difference between twose distributions.

#### Requirements
* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)


#### Usage
    python3 plotter.py DATA1 DATA2
where `DATA1` and `DATA2` are paths to the JSON files containing the datasets that are to be plotted.


#### How it works
The code reduces the colors into the 8 3-bit colors that are considered in our study and plots the precentage of each color in either dataset using matplotlib. It then calculates the difference between the distributions and plots it as well.

---

### color-distribution-distance.py
Calculates the distance between the color distributions of the two given datasets.

#### Requirements
* [numpy](https://numpy.org/)


#### Usage
    $ python3 DATA1 DATA2
where `DATA1` and `DATA2` are paths to the JSON files containing the datasets that are to be compared.


#### How it works
It divides the RGB colorspace into 8 congruent cubes, effectively reducing it to a 3-bit colorspace. Then it counts the percentage of datapoints that fall into each cube in each dataset and sums up the differences between the values of the corresponing cubes.
