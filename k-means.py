import math 
import random
import numpy as np
import matplotlib.pyplot as plt


def euclidean_distance(x, y):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

#points = [(1, 1), (2, 1), (4, 3), (5, 4)]]
points=[]
for i in range(200):
    points.append((random.randint(0,1000000000000),random.randint(0,1000000000000)))


k = 7
# centroids[i] = [x, y]
centroids = {}
for i in range(k):
    centroids[i] = points[i]


for i in range(10):
    classes = {}
    for i in range(k):
        classes[i] = []
    for point in points:
        distances = [euclidean_distance(point, centroids[centroid]) for centroid in centroids]
        classification = distances.index(min(distances))
        classes[classification].append(point)
    prev_centroids = dict(centroids)
    for classification in classes:
        centroids[classification] = np.average(classes[classification], axis=0)
    optimized = True
    for c in centroids:
        original_centroid = prev_centroids[c]
        current_centroid = centroids[c]
        if np.sum((current_centroid - original_centroid)/original_centroid * 100.0) > 0.01:
            print(np.sum((current_centroid - original_centroid)/original_centroid * 100.0))
            optimized = False
    if optimized:
        break

colors = 10*["g","r","c","b","k","y","m"]

for centroid in centroids:
    plt.scatter(centroids[centroid][0], centroids[centroid][1], marker="o", color="k", s=150, linewidths=5)

for classification in classes:
    color = colors[classification]
    for features in classes[classification]:
        plt.scatter(features[0], features[1], marker="x", color=color, s=150, linewidths=5)

plt.show()



