import random
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def distance(p1, p2):
    """Finds the euclidean distance between 2 points"""
    return np.sum(np.power(p2 - p1, 2))

def find_nearest_neighbors(point, otherPoints, k):
    """Finds the indexes of the k nearest neighbors of a point p among otherPoints"""

    distances = np.zeros(otherPoints.shape[0])

    for i in range(len(distances)):
        distances[i] = distance(point, otherPoints[i])

    nearestPointsIndex = np.argsort(distances)
    return nearestPointsIndex[:k]

def majority_vote(votes):
    """Finds the most commonly votes element"""

    vote_counts = {}

    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1 

    max_count = max(vote_counts.values())
    winners = []

    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)

    return random.choice(winners)

def predict_class(point, otherPoints, classes, k):
    """Predict the classification of the point according to its k nearest neighbors"""

    nearestPointsIndex = find_nearest_neighbors(point, otherPoints, k)
    return majority_vote(classes[nearestPointsIndex])

def generate_synth_data(n):
    """Generates random set of n points with their classes"""
    
    points = np.concatenate((ss.norm(0, 1).rvs((n, 2)), ss.norm(1, 1).rvs((n, 2))), axis = 0)
    classes = np.concatenate((np.repeat(0, n), np.repeat(0, n)))

    return (points, classes)

def make_prediction_grid(predictors, classes, limits, h, k):
    """Classify each point on the prediction grid."""
    
    (x_min, x_max, y_min, y_max) = limits

    Xs = np.arange(x_min, x_max, h)
    Ys = np.arange(y_min, y_max, h)

    X, Y = np.meshgrid(Xs, Ys)

    prediction_grid = np.zeros(X.shape, dtype = int)

    for i, x in enumerate(Xs):
        for j, y in enumerate(Ys):
            prediction_grid[j, i] = predict_class(np.array([x, y]), predictors, classes, k)

    return (X, Y, prediction_grid)

def plot_prediction_grid(X, Y, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""   

    background_colormap = ListedColormap(["hotpink", "lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap(["red", "blue", "green"])
    
    plt.figure(figsize = (10, 10))
    plt.pcolormesh(X, Y, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:, 0], predictors[:, 1], c = classes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1')
    plt.ylabel('Variable 2')
    plt.xticks(()) 
    plt.yticks(())
    plt.xlim(np.min(X), np.max(X))
    plt.ylim(np.min(Y), np.max(Y))
    plt.savefig(filename)

(predictors, classes) = generate_synth_data(50)

limits = (-3, 4, -3, 4)
h = 0.1

#(X, Y, prediction_grid) = make_prediction_grid(predictors, classes, limits, h, 5)

plot_file_name = "C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 3/K-Nearest Neighbors/prediction_grid_5.pdf"
#plot_prediction_grid(X, Y, prediction_grid, plot_file_name)


limits = (-3, 4, -3, 4)
h = 0.1

#(X, Y, prediction_grid) = make_prediction_grid(predictors, classes, limits, h, 50)

plot_file_name = "C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 3/K-Nearest Neighbors/prediction_grid_50.pdf"
#plot_prediction_grid(X, Y, prediction_grid, plot_file_name)